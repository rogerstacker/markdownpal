from markdownpal import MarkdownDocument
from markdownpal.blocks import (
    H1Block, H2Block, TextBlock, CodeBlock,
    TableBlock, ULBlock, HRBlock, ImageBlock
)
from markdownpal.inline import bold, italic


def test_full_document_render():
    doc = MarkdownDocument()
    doc.append(H1Block("项目文档"))
    doc.append(TextBlock(f"这是一个{bold('重要')}的说明段落。"))
    doc.append(H2Block("代码示例"))
    doc.append(CodeBlock("print('hello world')", lang="python"))
    doc.append(HRBlock())
    doc.append(TableBlock(
        headers=["功能", "状态"],
        rows=[["输出 MD", "✅"], ["输出 HTML", "❌"]]
    ))
    doc.append(ULBlock(["简单", "可扩展", "零依赖"]))

    expected = (
        "# 项目文档\n\n"
        "这是一个**重要**的说明段落。\n\n"
        "## 代码示例\n\n"
        "```python\n"
        "print('hello world')\n"
        "```\n\n"
        "---\n\n"
        "| 功能 | 状态 |\n"
        "| --- | --- |\n"
        "| 输出 MD | ✅ |\n"
        "| 输出 HTML | ❌ |\n\n"
        "- 简单\n- 可扩展\n- 零依赖"
    )
    assert doc.render() == expected


def test_full_document_save(tmp_path):
    doc = MarkdownDocument()
    doc.append(H1Block("Save Test"))
    doc.append(TextBlock("Written to file."))
    out = tmp_path / "result.md"
    doc.save(str(out))
    content = out.read_text(encoding="utf-8")
    assert content == "# Save Test\n\nWritten to file."
