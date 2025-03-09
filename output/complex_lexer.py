
import re
from src.regex_parse import parse_regex

class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.tokens = []
        self.errors = []
        self.token_definitions = {
        "digit": r"[0-9]",
        "letter": r"[a-zA-Z_]",
        "id": r"letter (letter | digit)*",
        "number": r"digit+",
        "float": r"digit+ '.' digit+",
        "string": r"'"' (_ # '"')* '"' | "'" (_ # "'")* "'"",
        "triple_string": r"'"""' (_ # '"""')* '"""' | "'''" (_ # "'''")* "'''"",
        "comment": r"'#' (_ # '\n')*",
        "keyword": r"'if' | 'else' | 'elif' | 'while' | 'for' | 'def' | 'return' | 'import' | 'from' |"
        }
        self.token_rules = [
        (r"[' ' '\t']", "return None"),
        (r"'\n'", "return EOL"),
        (r"comment", "return None"),
        (r"keyword", "return KEYWORD"),
        (r"number", "return INT"),
        (r"float", "return FLOAT"),
        (r"string", "return STRING"),
        (r"triple_string", "return STRING"),
        (r"'+'", "return PLUS"),
        (r"'-'", "return MINUS"),
        (r"'*'", "return TIMES"),
        (r"'**'", "return POWER"),
        (r"'/'", "return DIV"),
        (r"'//'", "return FLOOR_DIV"),
        (r"'%'", "return MOD"),
        (r"'='", "return ASSIGN"),
        (r"'=='", "return EQ"),
        (r"'!='", "return NE"),
        (r"'<'", "return LT"),
        (r"'>'", "return GT"),
        (r"'<='", "return LE"),
        (r"'>='", "return GE"),
        (r"'('", "return LPAREN"),
        (r"')'", "return RPAREN"),
        (r"'['", "return LBRACKET"),
        (r"']'", "return RBRACKET"),
        (r"'{'", "return LBRACE"),
        (r"'}'", "return RBRACE"),
        (r"':'", "return COLON"),
        (r"','", "return COMMA"),
        (r"'.'", "return DOT"),
        (r"'and'", "return AND"),
        (r"'or'", "return OR"),
        (r"'not'", "return NOT"),
        (r"id", "return IDENTIFIER"),
        (r"eof", "raise('Fin de buffer')"),
        (r".", "raise('Error léxico: Caracter no reconocido' + lxm)"),
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
                    if token_name is None:
                        pass  # Ignorar espacios o comentarios
                    elif token_name == "ERROR":
                        self.errors.append(f"Error léxico en posición {pos}: {lexeme}")
                    else:
                        self.tokens.append((token_name, lexeme))
                    pos += len(lexeme)
                    break
            if not match:
                raise ValueError(f"Error léxico en posición {pos}: {self.input_text[pos]}")
        return self.tokens, self.errors
    
    def print_tokens(self):
        if self.tokens:
            print("Tokens encontrados:")
            for token_name, lexeme in self.tokens:
                print(f"  - {token_name}: '{lexeme}'")
        else:
            print("No se identificaron tokens.")
    
    def print_errors(self):
        if self.errors:
            print("Errores léxicos detectados:")
            for pos, lexeme in self.errors:
                print(f"  - Error en posición {pos}: '{lexeme}'")
        else:
            print("No se detectaron errores léxicos.")
    
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
