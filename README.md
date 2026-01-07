# Mini Compiler Project (Python)

This repository contains a simple compiler built step-by-step in Python.
The goal is to learn how a compiler works by implementing each major stage in a clean, modular, and extendable way.

Current progress: **Lexer (Tokenization) complete**
Next steps: Parser → AST → Interpreter → Error System → Codegen

---

## Overview of Compiler Stages

This compiler will eventually include:

1. Lexer (Tokenization) ✔ Completed
2. Parser (Syntax Analysis) ☐ Upcoming
3. AST (Abstract Syntax Tree) ☐ Planned
4. Interpreter / Evaluator ☐ Planned
5. Error Handling System ☐ Planned
6. Code Generation / Virtual Machine ☐ Future

Right now, the repository focuses on **only the lexer**, but the structure is designed to grow as more parts are added.

---

## Repository Structure (Current)

```
Compiler/
│
├── main.py        # Lexer implementation & run() helper
├── shell.py       # REPL shell for testing the lexer
└── README.md      # Documentation
```

As the project grows, it will look like:

```
Compiler/
│
├── lexer/
├── parser/
├── ast/
├── interpreter/
├── errors/
└── README.md
```

---

## What the Lexer Does

The lexer converts raw text input into meaningful tokens.
It currently supports:

* Integer literals
* * operator
* * operator
* Whitespace skipping
* Basic error reporting

### Example

Input:

```
12 + 5 - 3
```

Output:

```
[t_int:12, plus:+, t_int:5, minus:-, t_int:3]
```

---

## How the Lexer Works

1. Reads characters one-by-one
2. Groups digits into complete numbers
3. Converts + and - into operator tokens
4. Skips spaces and tabs
5. Detects illegal characters
6. Produces a clean token list for the parser

The parser (coming later) will turn these tokens into an AST.

---

## Running the Shell (REPL)

To start the interactive shell:

```
python shell.py
```

You'll see:

```
MiniShell v1.0
Type 'exit' to quit.
>>>
```

Try:

```
>>> 45 + 7 - 2
[t_int:45, plus:+, t_int:7, minus:-, t_int:2]
```

To exit:

```
>>> exit
```

---

## main.py (Lexer Implementation Summary)

`main.py` includes:

* Token type definitions
* Token class
* Lexer class
* run() function used by shell.py

Example token output:

```
t_int:10
plus:+
```

---

## Future Improvements (Planned Roadmap)

### Part 2 – Parser

* Parse arithmetic expressions
* Build grammar
* Handle operator precedence

### Part 3 – AST Nodes

* NumberNode
* BinOpNode
* UnaryOpNode

### Part 4 – Interpreter

* Evaluate expressions
* Add variables (`x = 5`)
* Support expression evaluation

### Part 5 – Error System

* Lexer errors
* Parser errors
* Runtime errors with position info

### Part 6 – Code Generator / VM

* Bytecode generation
* Virtual machine execution
* Optional: transpile to Python or C

---

## Purpose of This Project

This project helps you understand:

* How compilers break code into stages
* How lexers and parsers work
* How interpreters evaluate expressions
* How programming languages are built

It’s designed to be beginner-friendly but expandable.

---

## Contributing / Extending

As more components (Parser, AST, Interpreter) are built, update the README sections.
The design is intentionally modular to allow easy expansion.

