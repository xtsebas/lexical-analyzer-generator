import re

class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.tokens = []
        self.token_definitions = {
        "digit": r"['0'-'9']",
        "letter": r"['a'-'z' 'A'-'Z']",
        "id": r"letter (letter | digit)*",
        "number": r"digit+",
        "string": r"'"' (letter | digit | ' ' | [!-/])* '"'",
        "float": r"digit+ '.' digit+",
        "comment": r"'(*' (_ # '*)')* '*)'"
        }
        self.token_rules = [
        (r"[' ' '\t']", "return lexbuf"),
        (r"| '\n'", "return EOL"),
        (r"| number", "return int(lxm)"),
        (r"| float", "return FLOAT"),
        (r"| string", "return STRING"),
        (r"| comment", "return lexbuf"),
        (r"| '+'", "return PLUS"),
        (r"| '-'", "return MINUS"),
        (r"| '*'", "return TIMES"),
        (r"| '/'", "return DIV"),
        (r"| '('", "return LPAREN"),
        (r"| ')'", "return RPAREN"),
        (r"| id", "return IDENTIFIER"),
        (r"| '='", "return ASSIGN"),
        (r"| ';'", "return SEMICOLON"),
        (r"| '<'", "return LT"),
        (r"| '>'", "return GT"),
        (r"| '<='", "return LE"),
        (r"| '>='", "return GE"),
        (r"| '=='", "return EQ"),
        (r"| '!='", "return NE"),
        (r"| eof", "raise('Fin de buffer')")
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
                raise ValueError(f"Error léxico en posición {pos}: {self.input_text[pos]}")
        return self.tokens

if __name__ == "__main__":
    text = input("Ingrese el código a analizar: ")
    lexer = Lexer(text)
    tokens = lexer.tokenize()
    print("Tokens encontrados:", tokens)
