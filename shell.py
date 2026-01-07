from lexer import run

while True:
    text = input(">>> ")

    if text.lower() == "exit":
        break

    tokens, error = run(text)

    if error:
        print("ERROR:", error)
    else:
        print(tokens)