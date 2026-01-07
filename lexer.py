# TOKEN

digits = '0123456789'
t_int = 't_int'
t_plus = 'plus'
t_minus = 'minus'


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value is not None:
            return f'{self.type}:{self.value}'
        return f'{self.type}'

# LEXER

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None  # END OF INPUT

    def make_tokens(self):
        tokens = []

        while self.current_char is not None:

            if self.current_char in ' \t':
                self.advance()

            elif self.current_char in digits:
                tokens.append(self.make_number())

            elif self.current_char == '+':
                tokens.append(Token(t_plus, '+'))
                self.advance()

            elif self.current_char == '-':
                tokens.append(Token(t_minus, '-'))
                self.advance()

            else:
                return [], f"Illegal character '{self.current_char}'"

        return tokens, None

    def make_number(self):
        num_str = ''

        while self.current_char is not None and self.current_char in digits:
            num_str += self.current_char
            self.advance()

        return Token(t_int, int(num_str))

# RUN FUNCTION

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    return tokens, error
