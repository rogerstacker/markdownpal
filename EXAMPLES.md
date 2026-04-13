# MarkdownPal Examples

## Quick Start

```python
from markdownpal import Document
from markdownpal.blocks import H1Block, TextBlock
from markdownpal.inline import bold

doc = Document()
doc.append(H1Block("Hello, MarkdownPal"))
doc.append(TextBlock(f"Build {bold('Markdown')} files with Python."))
doc.save("output.md")
```

---

## Block Types

### Headings

```python
from markdownpal.blocks import H1Block, H2Block, H3Block, H4Block, H5Block, H6Block

doc.append(H1Block("Title"))        # # Title
doc.append(H2Block("Section"))      # ## Section
doc.append(H3Block("Subsection"))   # ### Subsection
doc.append(H4Block("Detail"))       # #### Detail
doc.append(H5Block("Minor"))        # ##### Minor
doc.append(H6Block("Tiny"))         # ###### Tiny
```

### Text & Formatting

```python
from markdownpal.blocks import TextBlock, QuoteBlock, HRBlock, CommentBlock
from markdownpal.inline import bold, italic, code, strikethrough

doc.append(TextBlock("Plain paragraph."))
doc.append(TextBlock(f"{bold('Bold')}, {italic('italic')}, {code('inline code')}, {strikethrough('struck')}."))
doc.append(QuoteBlock("A quote that spans\nmultiple lines."))
doc.append(HRBlock())
doc.append(CommentBlock("This comment is invisible in rendered output."))
```

### Code

```python
from markdownpal.blocks import CodeBlock

doc.append(CodeBlock("print('hello world')", lang="python"))
doc.append(CodeBlock("SELECT * FROM users;", lang="sql"))
doc.append(CodeBlock("plain code block, no highlighting"))
```

### Lists

```python
from markdownpal.blocks import ULBlock, OLBlock, TaskListBlock

doc.append(ULBlock(["Apples", "Bananas", "Cherries"]))

doc.append(OLBlock(["Install", "Configure", "Run"]))

doc.append(TaskListBlock([
    ("Write tests", True),
    ("Write code", True),
    ("Deploy", False),
]))
```

### Table

```python
from markdownpal.blocks import TableBlock

doc.append(TableBlock(
    headers=["Name", "Role", "Status"],
    rows=[
        ["Alice", "Engineer", "✅ Active"],
        ["Bob",   "Designer", "✅ Active"],
        ["Carol", "PM",       "🔄 Onboarding"],
    ]
))
```

### Images & Links

```python
from markdownpal.blocks import ImageBlock, LinkBlock

doc.append(ImageBlock(src="https://example.com/logo.png", alt="Project Logo"))
doc.append(ImageBlock(src="diagram.png"))  # alt is optional
doc.append(LinkBlock(text="Documentation", url="https://example.com/docs"))
```

---

## Inline Helpers

Inline helpers return strings and can be composed or embedded inside any block content:

```python
from markdownpal.inline import bold, italic, code, strikethrough

bold("important")            # **important**
italic("note")               # *note*
code("os.path.join()")       # `os.path.join()`
strikethrough("deprecated")  # ~~deprecated~~

# Composable
bold(italic("emphasis"))     # ***emphasis***

# Embed in blocks
TextBlock(f"See {code('render()')} for details.")
H2Block(f"API {italic('Reference')}")
```

---

## Render to String

Use `render()` to get the Markdown string directly without saving to disk:

```python
doc = MarkdownDocument()
doc.append(H1Block("Report"))
doc.append(TextBlock("Generated automatically."))

output = doc.render()
print(output)
# # Report
#
# Generated automatically.
```

---

## Save to File

```python
doc.save("report.md")              # relative path
doc.save("/tmp/docs/report.md")    # absolute path
```

Files are written in UTF-8 and fully support international characters and emoji:

```python
doc.append(H1Block("项目文档"))
doc.append(TextBlock("支持中文、日本語、한국어 및 emoji 🎉"))
doc.save("国际化.md")
```

---

## Complete Example

```python
from markdownpal import Document
from markdownpal.blocks import (
    H1Block, H2Block, H3Block,
    TextBlock, CodeBlock, TableBlock,
    ULBlock, TaskListBlock, HRBlock,
)
from markdownpal.inline import bold, italic, code

doc = Document()

doc.append(H1Block("Project Changelog"))
doc.append(TextBlock(f"All notable changes are documented here. Format based on {bold('Keep a Changelog')}."))
doc.append(HRBlock())

doc.append(H2Block("v1.2.0 — 2026-04-12"))
doc.append(H3Block("Added"))
doc.append(ULBlock([
    f"{code('TaskListBlock')} for checkbox lists",
    "UTF-8 file output via save()",
    "Inline helpers: bold, italic, code, strikethrough",
]))

doc.append(H3Block("Fixed"))
doc.append(ULBlock([
    f"{code('QuoteBlock')} now correctly handles multi-line text",
]))

doc.append(H2Block("Compatibility"))
doc.append(TableBlock(
    headers=["Python", "Supported"],
    rows=[
        ["3.9", "✅"],
        ["3.10", "✅"],
        ["3.11", "✅"],
        ["3.12", "✅"],
    ]
))

doc.append(H2Block("Installation"))
doc.append(CodeBlock("pip install markdownpal", lang="bash"))

doc.save("CHANGELOG.md")
```
