# Plantilla base para el analizador léxico generado
LEXER_TEMPLATE = """import re

class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.tokens = []
        self.token_definitions = {{
{token_definitions}
        }}
        self.token_rules = [
{token_rules}
        ]

    def tokenize(self):
        pos = 0
        while pos < len(self.input_text):
            match = None
            for pattern, token_name in self.token_rules:
                regex = re.compile(pattern)
                match = regex.match(self.input_text, pos)
                if match:
                    lexeme = match.group(0)
                    self.tokens.append((token_name, lexeme))
                    pos += len(lexeme)
                    break
            if not match:
                raise ValueError(f"Error léxico en posición {{pos}}: {{self.input_text[pos]}}")
        return self.tokens

if __name__ == "__main__":
    text = input("Ingrese el código a analizar: ")
    lexer = Lexer(text)
    tokens = lexer.tokenize()
    print("Tokens encontrados:", tokens)
"""