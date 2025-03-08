import re

class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.tokens = []
        self.token_definitions = {
        "digit": r"['0'-'9']",
        "letter": r"['a'-'z' 'A'-'Z']",
        "id": r"letter (letter | digit)*",
        "number": r"digit+"
        }
        self.token_rules = [
        (r"[' ' '\t']", "return lexbuf"),
        (r"| '\n'", "return EOL"),
        (r"| number", "return int(lxm)"),
        (r"| '+'", "return PLUS"),
        (r"| '-'", "return MINUS"),
        (r"| '*'", "return TIMES"),
        (r"| '/'", "return DIV"),
        (r"| '('", "return LPAREN"),
        (r"| ')'", "return RPAREN"),
        (r"| id", "return IDENTIFIER"),
        (r"| eof", "raise('Fin de buffer')"),
        (r"| .", "raise('Error léxico: Caracter no reconocido'  + lxm)"),
        (r".", "ERROR")
        ]

    def lex_analyze(self):
        pos = 0
        while pos < len(self.input_text):
            match = None
            for pattern, token_name in self.token_rules:
                regex = re.compile(pattern)
                match = regex.match(self.input_text, pos)
                if match:
                    lexeme = match.group(0)
                    if token_name == "ERROR":
                        self.errors.append(f"Error léxico en posición {pos}: {lexeme}")
                    else:
                        self.tokens.append((token_name, lexeme))
                    pos += len(lexeme)
                    break
            if not match:
                raise ValueError(f"Error léxico en posición {pos}: {self.input_text[pos]}")
        return self.tokens, self.errors

if __name__ == "__main__":
    text = input("Ingrese el código a analizar: ")
    lexer = Lexer(text)
    tokens, errors = lexer.tokenize()
    print("Tokens encontrados:", tokens)
    if errors:
        print("Errores léxicos detectados:")
        for error in errors:
            print(error)
