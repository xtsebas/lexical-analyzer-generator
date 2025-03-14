# Plantilla base para el analizador lexico generado
LEXER_TEMPLATE = """
from src.regex_parse import parse_regex

class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.tokens = []
        self.errors = []
        self.token_definitions = {{
{token_definitions}
        }}
        self.token_rules = [
{token_rules}
        ]

    def lex_analyze(self):
        pos = 0
        while pos < len(self.input_text):
            match = None
            for pattern, token_name in self.token_rules:
                # Verificar si el lexema coincide con el patrón usando parse_regex
                lexeme = self._get_lexeme(pos, pattern)
                if lexeme:
                    if token_name is None:
                        pass  # Ignorar espacios o comentarios
                    elif token_name == "ERROR":
                        self.errors.append(f"Error lexico en posicion {{pos}}: {{lexeme}}")
                    else:
                        self.tokens.append((token_name, lexeme))
                    pos += len(lexeme)
                    break
            if not match:
                raise ValueError(f"Error lexico en posicion {{pos}}: {{self.input_text[pos]}}")
        return self.tokens, self.errors

    def _get_lexeme(self, pos: int, pattern: str) -> str:
        max_lexeme = ""
        for end_pos in range(pos + 1, len(self.input_text) + 1):
            lexeme = self.input_text[pos:end_pos]
            if parse_regex(lexeme, pattern):
                if len(lexeme) > len(max_lexeme):
                    max_lexeme = lexeme
        return max_lexeme if max_lexeme else None
    
    def print_tokens(self):
        if self.tokens:
            print("Tokens encontrados:")
            for token_name, lexeme in self.tokens:
                print(f"  - {{token_name}}: '{{lexeme}}'")
        else:
            print("No se identificaron tokens.")
    
    def print_errors(self):
        if self.errors:
            print("Errores lexicos detectados:")
            for pos, lexeme in self.errors:
                print(f"  - Error en posicion {{pos}}: '{{lexeme}}'")
        else:
            print("No se detectaron errores lexicos.")
    
    def verify_lexeme(self, lexeme):
        for token_name, regex in self.token_definitions.items():
            if parse_regex(lexeme, regex):
                return token_name
        return None

def lexical_analyzer(text):
    lexer = Lexer(text)
    lexer.lex_analyze()
    lexer.print_tokens()
    lexer.print_errors()
"""