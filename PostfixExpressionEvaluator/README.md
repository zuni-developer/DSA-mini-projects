# 📬 Postfix Expression Evaluator

A simple Python program that evaluates mathematical expressions written in **postfix notation** (also known as Reverse Polish Notation).

## 📌 What is Postfix Notation?

In postfix notation, operators come **after** their operands. For example:

```
3 4 +      => 3 + 4 = 7  
5 1 2 + 4 * + 3 -   => 5 + ((1 + 2) * 4) - 3 = 14
```

## 🚀 Features

- Handles basic arithmetic operations: `+`, `-`, `*`, `/`, `^`
- Evaluates space-separated postfix expressions
- Stack-based logic for accurate and efficient computation
- Includes a test suite with multiple test cases

## 🛠️ Usage

### 1. Run the Program

```bash
python PostfixEvaluator.py
```

You will be prompted to enter a postfix expression:

```
Enter postfix expression (space-separated): 3 4 + 2 *
Result: 14
```

### 2. Run Test Cases

To automatically test common expressions:

```bash
python test_cases.py
```

If you have a `run_tests()` function in `__main__`, it will run all tests and display pass/fail results.

## 🧪 Example Test Cases

| Expression              | Result |
|-------------------------|--------|
| `3 4 +`                 | 7      |
| `10 5 /`                | 2      |
| `2 3 4 * +`             | 14     |
| `5 1 2 + 4 * + 3 -`     | 14     |
| `2 3 ^`                 | 8      |
| `6 2 / 3 - 4 2 * +`     | 8      |
| `100 200 + 2 / 5 * 7 +` | 757    |

## 🧠 How It Works

- Operands are pushed to a stack.
- When an operator is encountered, the top two values are popped, the operation is applied, and the result is pushed back.
- Final result is popped from the stack.
