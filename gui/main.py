import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.generator import generate_lexer

# Ejecuta la generación del analizador desde la GUI
# Input: Ninguno
# Output: archivo generado en output/
def run_generator_from_gui():
    print("Parseando archivos .yal a Json ...")
    generate_lexer()
    print("\nGenerados los analizadores lexicos")

if __name__ == "__main__":
    run_generator_from_gui()