# MarkdownPal

A pure-Python library for programmatically generating Markdown (`.md`) files via a clean, block-based document builder API.

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Features

- **Block-based API** — compose documents from typed, self-contained block objects
- **Inline formatting helpers** — `bold()`, `italic()`, `code()`, `strikethrough()`
- **Full block support** — headings, paragraphs, quotes, code, lists, tables, images, links
- **Save to file** — UTF-8 output with full support for international characters and emoji
- **Zero dependencies** — no third-party packages required
- **Python 3.9+**

---

## Installation

```bash
pip3 install markdownpal
```

---

## Quick Start

```python
from markdownpal import Document
from markdownpal.blocks import H1Block, H2Block, TextBlock, CodeBlock, ULBlock
from markdownpal.inline import bold

doc = Document()

doc.append(H1Block("My Project"))
doc.append(TextBlock(f"A {bold('simple')} example of MarkdownPal."))
doc.append(H2Block("Installation"))
doc.append(CodeBlock("pip install markdownpal", lang="bash"))
doc.append(H2Block("Features"))
doc.append(ULBlock(["Zero dependencies", "Clean API", "Python 3.9+"]))

doc.save("output.md")
```

Output (`output.md`):

```markdown
# My Project

A **simple** example of MarkdownPal.

## Installation

```bash
pip install markdownpal
```

## Features

- Zero dependencies
- Clean API
- Python 3.9+
```

---

## Block Reference

### Headings

```python
from markdownpal.blocks import H1Block, H2Block, H3Block, H4Block, H5Block, H6Block

doc.append(H1Block("Title"))       # # Title
doc.append(H2Block("Section"))     # ## Section
doc.append(H3Block("Subsection"))  # ### Subsection
```

### Text

```python
from markdownpal.blocks import TextBlock, QuoteBlock, HRBlock, CommentBlock

doc.append(TextBlock("A plain paragraph."))
doc.append(QuoteBlock("A blockquote.\nSpanning multiple lines."))
doc.append(HRBlock())                               # ---
doc.append(CommentBlock("Hidden in rendered output."))  # <!-- ... -->
```

### Code

```python
from markdownpal.blocks import CodeBlock

doc.append(CodeBlock("print('hello')", lang="python"))
doc.append(CodeBlock("SELECT * FROM users;", lang="sql"))
doc.append(CodeBlock("no language specified"))
```

### Lists

```python
from markdownpal.blocks import ULBlock, OLBlock, TaskListBlock

doc.append(ULBlock(["Apples", "Bananas", "Cherries"]))

doc.append(OLBlock(["Install", "Configure", "Run"]))

doc.append(TaskListBlock([
    ("Write tests", True),
    ("Write code", True),
    ("Deploy",      False),
]))
```

### Table

```python
from markdownpal.blocks import TableBlock

doc.append(TableBlock(
    headers=["Name", "Role", "Status"],
    rows=[
        ["Alice", "Engineer", "Active"],
        ["Bob",   "Designer", "Active"],
    ]
))
```

### Images & Links

```python
from markdownpal.blocks import ImageBlock, LinkBlock

doc.append(ImageBlock(src="logo.png", alt="Project Logo"))
doc.append(LinkBlock(text="Documentation", url="https://example.com/docs"))
```

---

## Inline Helpers

Inline helpers return plain strings and can be embedded inside any block content:

```python
from markdownpal.inline import bold, italic, code, strikethrough

bold("important")            # **important**
italic("note")               # *note*
code("os.path.join()")       # `os.path.join()`
strikethrough("deprecated")  # ~~deprecated~~

# Composable
bold(italic("emphasis"))     # ***emphasis***

# Embed in blocks
doc.append(TextBlock(f"Call {code('render()')} to get the output string."))
```

---

## Document API

```python
doc = Document()
doc.append(block)   # Add a Block instance
doc.render()        # Returns the full Markdown string
doc.save("out.md")  # Writes UTF-8 Markdown file to disk
```

`append()` raises `TypeError` if the argument is not a `Block` instance.  
`render()` joins all blocks with a blank line (`\n\n`) between them.

---

## Project Structure

```
markdownpal/
├── __init__.py          # Top-level public API
├── document.py          # Document class
├── inline.py            # Inline format helpers
└── blocks/
    ├── base.py          # Block abstract base class
    ├── heading.py       # H1Block ~ H6Block
    ├── text.py          # TextBlock, QuoteBlock, HRBlock, CommentBlock
    ├── code.py          # CodeBlock
    ├── list_.py         # ULBlock, OLBlock, TaskListBlock
    ├── table.py         # TableBlock
    └── media.py         # ImageBlock, LinkBlock
```

---

## Development

```bash
# Clone the repository
git clone https://github.com/rogerstacker/markdownpal.git
cd markdownpal

# Install dev dependencies
pip3 install -e ".[dev]"

# Run tests
pytest
```

---

## License

[MIT](LICENSE) © 2026 Rogerstacker
