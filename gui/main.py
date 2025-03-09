import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.generator import generate_lexer
from output import simple_lexer, medium_lexer, complex_lexer

def read_input_file(filename):
    abs_path = os.path.abspath(filename)
    print(f"Buscando archivo en: {abs_path}")  # Debugging

    if not os.path.exists(abs_path):
        print(f"Error: El archivo '{abs_path}' no se encontro.")
        return None
    
    try:
        with open(abs_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error al leer el archivo '{abs_path}': {e}")
        return None


def run_lexer_from_file(filename):
    input_text = read_input_file(filename)
    if input_text is not None:
        lexer = simple_lexer.Lexer(input_text)
        tokens, errors = lexer.lex_analyze()

        print("\n=== TOKENS ENCONTRADOS ===")
        lexer.print_tokens()

        print("\n=== ERRORES LEXICOS ===")
        lexer.print_errors()

# Ejecuta la generación del analizador desde la GUI
# Input: Ninguno
# Output: archivo generado en output/
def run_generator_from_gui():
    print("Parseando archivos .yal a Json ...")
    generate_lexer()

if __name__ == "__main__":
    run_generator_from_gui()
    input_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "examples", "input_medium.txt"))
    run_lexer_from_file(input_file)