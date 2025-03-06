import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import re
import json

# Genera el analizador léxico en base a un archivo .yal
# Input: ruta del archivo .yal
# Output: archivo Python con el analizador léxico generado
def generate_lexer(yal_file):
 pass

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
            let_match = re.match(r"let (\w+)\s*=\s*(.+)", line)
            if let_match:
                name, regex = let_match.groups()
                self.definitions[name] = regex
                continue

            # Detectar el inicio de la sección rule
            if line.startswith("rule "):
                in_rule_section = True
                continue

            # Extraer reglas léxicas en la sección rule
            if in_rule_section:
                rule_match = re.match(r"(.+)\s+\{(.+)\}", line)
                if rule_match:
                    token, action = rule_match.groups()
                    self.rules.append((token.strip(), action.strip()))


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
            "rules": self.rules
        }

        with open(output_filename, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        print(f"Guardado: {output_filename}")


# Procesar archivos .yal con YAlexParser
# Input: input_dir, output_dir
# Output: 
def process_yalex_files(input_dir="examples/", output_dir="data/"):
    """Procesa todos los archivos .yal en input_dir y guarda los resultados en output_dir"""
    for filename in os.listdir(input_dir):
        if filename.endswith(".yal"):
            parser = YALexParser(os.path.join(input_dir, filename))
            parser.parse()
            parser.save_to_json(output_dir)