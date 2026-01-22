from lexer import run
from parser import Parser

while True:
    text = input(">>> ")

    if text.lower() == "exit":
        break

    tokens, error = run(text)

    if error:
        print("ERROR:", error)
    else:
        parser = Parser(tokens)
        ast = parser.parse()
        print(ast)
