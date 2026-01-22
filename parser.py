from lexer import t_int, t_plus, t_minus

class NumberNode:
    def __init__(self, number_token):
        self.number_token = number_token

    def __repr__(self):
        return f"{self.number_token}"


class BinaryOperationNode:
    def __init__(self, left_node, operator_token, right_node):
        self.left_node = left_node
        self.operator_token = operator_token
        self.right_node = right_node

    def __repr__(self):
        return f"({self.left_node} {self.operator_token} {self.right_node})"


class Parser:
    def __init__(self, list_of_tokens):
        self.tokens = list_of_tokens
        self.current_token_index = -1
        self.current_token = None
        self.move_to_next_token()

    # Move pointer to next token
    def move_to_next_token(self):
        self.current_token_index += 1

        if self.current_token_index < len(self.tokens):
            self.current_token = self.tokens[self.current_token_index]
        else:
            self.current_token = None

        return self.current_token

    # Entry point of parser
    def parse(self):
        return self.parse_expression()

    # expression -> number ((+ or -) number)*
    def parse_expression(self):

        # First number
        left_node = self.parse_number()

        # While we see + or -
        while (
            self.current_token is not None
            and self.current_token.type in (t_plus, t_minus)
        ):

            operator_token = self.current_token
            self.move_to_next_token()

            right_node = self.parse_number()

            # Build tree node
            left_node = BinaryOperationNode(
                left_node,
                operator_token,
                right_node
            )

        return left_node

    # number → INT
    def parse_number(self):

        token = self.current_token

        if token.type == t_int:
            self.move_to_next_token()
            return NumberNode(token)

        raise Exception("Expected a number")
