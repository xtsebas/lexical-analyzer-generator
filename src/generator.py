import os
import sys
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.lexer_template import LEXER_TEMPLATE

# Procesar archivos .yal con YAlexParser
# Input: input_dir, output_dir
# Output: 
def generate_lexer(input_dir="examples/", output_dir="data/", output_dir_py="output/"):
    """Procesa todos los archivos .yal en input_dir y guarda los resultados en output_dir"""
    for filename in os.listdir(input_dir):
        if filename.endswith(".yal"):
            parser = YALexParser(os.path.join(input_dir, filename))
            parser.parse()
            parser.save_to_json(output_dir)
            generate_python_lexer(parser, output_dir_py)


#FUNCIONES Y CLASES PRIVADAS DEL MODULO
def generate_python_code(yalexParser):
    """Genera código Python usando la plantilla"""

    # Reemplazar referencias a otras reglas en self.token_definitions
    for key, value in yalexParser.definitions.items():
        for sub_key, sub_value in yalexParser.definitions.items():
            value = value.replace(sub_key, f"({sub_value})")  # Expande referencias
        yalexParser.definitions[key] = value

    # Corrección en la generación de expresiones regulares
    token_definitions = ",\n".join(f'        "{key}": r"{value}"' for key, value in yalexParser.definitions.items())

    # Manejo de token rules evitando errores de formato
    token_rules = []
    for pattern, action in yalexParser.rules:
        pattern = pattern.strip().replace("'", "")  # Eliminar comillas innecesarias
        pattern = pattern.replace("*", r"\*").replace("+", r"\+").replace("?", r"\?")
        pattern = pattern.replace("(", r"\(").replace(")", r"\)").replace("|", r"\|")
        pattern = pattern.replace("//", r"//").replace("**", r"\*\*")  # Escapar correctamente

        # Corregir expresión regular de comentarios
        if pattern.startswith("#"):
            pattern = r"#.*"

        # Reemplazar variables de token por sus expresiones reales
        for key, value in yalexParser.definitions.items():
            pattern = pattern.replace(key, value)

        token_rules.append(f'        (r"{pattern}", "{action}")')

    # Asegurar que las palabras clave son evaluadas antes que los identificadores
    token_rules.insert(0, '        (r"\\b(print|return|None|True|False)\\b", "return KEYWORD")')

    # Agregar regla para `=`
    token_rules.append('        (r"=", "return ASSIGN")')

    # Manejo de errores
    token_rules.append('        (r".", "raise(\'Error lexico: Caracter no reconocido \' + lxm)")')

    return LEXER_TEMPLATE.format(
        token_definitions=token_definitions,
        token_rules=",\n".join(token_rules)
    )


def generate_python_lexer(yalexParser, output_dir="output/"):
    """Genera código Python basado en el archivo YALex"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_filename = os.path.join(output_dir, os.path.basename(yalexParser.filename).replace(".yal", "_lexer.py"))
    
    python_code = generate_python_code(yalexParser)

    with open(output_filename, "w", encoding="utf-8") as py_file:
        py_file.write(python_code)

    print(f"Lexer generado: {output_filename}")


#Clase para generar un parsing del .Yal
class YALexParser:
    def __init__(self, filename):
        self.filename = filename
        self.header = ""
        self.definitions = {}
        self.rules = []

    # Leer archivo
    # Input: self
    # Output: file
    def read_file(self):
        """Lee el contenido del archivo YALex"""
        with open(self.filename, "r", encoding="utf-8") as file:
            return file.readlines()

    # Parsing del archivo yalex
    # Input: self
    # Output: 
    def parse(self):
        """Parsea el archivo YALex y extrae la información relevante"""
        lines = self.read_file()
        in_rule_section = False
        
        for line in lines: # Ir leyendo linea por linea
            line = line.strip()
            if not line or line.startswith("(*"):  # Ignorar comentarios y líneas vacías
                continue

            # Extraer el header
            if line.startswith("{") and "}" in line:
                self.header = line
                continue

            # Extraer definiciones de expresiones regulares (let ident = regexp)
            if line.startswith("let "):
                parts = line.split("=")
                if len(parts) == 2:
                    name = parts[0].replace("let", "").strip()
                    regex = parts[1].strip()
                    self.definitions[name] = regex
                continue

            # Detectar el inicio de la sección rule
            if line.startswith("rule "):
                in_rule_section = True
                continue

            # Extraer reglas léxicas en la sección rule
            if in_rule_section:
                if "{" in line and "}" in line:
                    parts = line.split("{")
                    token = parts[0].strip().lstrip('|').strip()
                    action = parts[1].split("}")[0].strip()
                    if action == "return lexbuf":
                        action = "return None"
                    self.rules.append((token, action))


    # Guardar el resultado en un json
    # Input: output_dir
    # Output: 
    def save_to_json(self, output_dir="data/"):
        """Guarda el resultado parseado en un archivo JSON en data/"""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)  # Crear carpeta si no existe
        
        output_filename = os.path.join(output_dir, os.path.basename(self.filename).replace(".yal", ".json"))
        data = {
            "filename": self.filename,
            "header": self.header,
            "definitions": self.definitions,
            "rules": self.rules,
            "errors": []
        }

        with open(output_filename, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        print(f"Guardado: {output_filename}")