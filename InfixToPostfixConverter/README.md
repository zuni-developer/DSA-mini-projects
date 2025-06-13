# InfixToPostfixConverter

A Python class to convert **infix expressions** to **postfix notation** (Reverse Polish Notation).  
This converter handles operands (numbers and letters), operators (`+`, `-`, `*`, `/`, `^`), and parentheses, respecting operator precedence and associativity.

---

## 📋 Features

- Supports multi-digit numbers and variables (e.g., `A`, `B`, `10`, `20`).
- Handles operator precedence:  
  `^` (highest), `*` and `/` (medium), `+` and `-` (lowest).
- Correctly processes parentheses to override precedence.
- Returns postfix expression as a concatenated string without spaces.

---

## ⚙️ Usage

You can use the `InfixToPostfix` class to convert any valid infix expression:

```python
from InfixToPostfixConverter import InfixToPostfix

converter = InfixToPostfix()
expr = "A+B*C"
converter.convert(expr)
postfix = converter.get_postfix()
print(f"Infix: {expr} ➜ Postfix: {postfix}")
# Output: Infix: A+B*C ➜ Postfix: ABC*+
