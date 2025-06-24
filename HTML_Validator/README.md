# 🧾 HTML Validator — Using Stacks and Queues

## 📌 What Is This?

This is a Python project that checks whether an HTML file is **well-formatted** — meaning all the opening and closing tags are matched properly and closed in the correct order.

You’ll be using **Stacks** and **Queues** to simulate how a browser might keep track of tags when rendering HTML.

---

## 🤔 Why Stacks and Queues?

- A **Queue** is used to read all the HTML tags in the order they appear — just like a browser parses from top to bottom.
- A **Stack** is used to keep track of currently open tags. This works well because the last tag that was opened should be the first one to close — classic **LIFO (Last-In-First-Out)** behavior.

---

## ⚙️ How It Works

### Step-by-Step:

1. The `html_reader.py` file reads an HTML file.
2. It uses the `HtmlTag.tokenize()` method to break it down into tags and puts them into a **Queue**.
3. The `is_valid_html()` method in `html_validator.py` processes these tags:
   - Every **opening tag** is pushed onto a **Stack**.
   - Every **closing tag** is checked against the top of the stack:
     - If it matches, the stack pops the opening tag.
     - If it doesn’t match, the HTML is invalid.
   - **Self-closing tags** like `<br/>` or `<img/>` are ignored.
4. At the end:
   - If the stack is empty → HTML is valid ✅
   - If not → HTML has unmatched opening tags ❌
   - If a closing tag appears with no opening match → ❌ return `None`

---

## 🧪 How To Run

### 👣 Steps:

1. Place an HTML file (like `sample.html`) in the same directory.

2. Create a Python script or use the example below:

```python
from html_reader import HtmlReader
from html_validator import HtmlValidator

tags = HtmlReader.get_tags_from_html_file("sample.html")
result = HtmlValidator.is_valid_html(tags)

if result is None:
    print("Invalid HTML: Unmatched closing tag found.")
elif result.is_empty():
    print("Valid HTML! All tags are matched.")
else:
    print("Invalid HTML: Unmatched opening tags left:")
    while not result.is_empty():
        print(result.pop())
```

3. Run it:

```bash
python your_script_name.py
```

---

## 🧠 Example Scenarios

### ✅ Well-Formatted

```html
<html><body><p>Hello</p></body></html>
```

Returns: Empty stack → Valid ✅

---

### ❌ Tags Closed in Wrong Order

```html
<html><body><p><b>Hello</p></b></body></html>
```

Returns: Stack with unmatched tags → Invalid ❌

---

### ❌ Closing Tag with No Opening

```html
<html><body>Hello</div></body></html>
```

Returns: `None` → Invalid ❌

---

## 🧑‍💻 Author

Made for learning how stacks and queues apply to real-world problems, especially parsing and validating HTML-like structures.

---

## ✅ Status

Fully working — just plug in your HTML files and test!

Happy debugging! 🐛
