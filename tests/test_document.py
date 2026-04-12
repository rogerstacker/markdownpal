from markdownpal.document import MarkdownDocument
from markdownpal.blocks import H1Block, TextBlock, HRBlock


def test_render_single_block():
    doc = MarkdownDocument()
    doc.append(H1Block("Hello"))
    assert doc.render() == "# Hello"


def test_render_multiple_blocks_separated_by_blank_line():
    doc = MarkdownDocument()
    doc.append(H1Block("Title"))
    doc.append(TextBlock("Body text"))
    assert doc.render() == "# Title\n\nBody text"


def test_render_empty_document():
    doc = MarkdownDocument()
    assert doc.render() == ""


def test_render_three_blocks():
    doc = MarkdownDocument()
    doc.append(H1Block("Title"))
    doc.append(HRBlock())
    doc.append(TextBlock("Content"))
    assert doc.render() == "# Title\n\n---\n\nContent"


def test_save_writes_file(tmp_path):
    doc = MarkdownDocument()
    doc.append(H1Block("Test"))
    out = tmp_path / "output.md"
    doc.save(str(out))
    assert out.read_text(encoding="utf-8") == "# Test"


def test_save_utf8_encoding(tmp_path):
    doc = MarkdownDocument()
    doc.append(TextBlock("你好世界"))
    out = tmp_path / "output.md"
    doc.save(str(out))
    assert out.read_text(encoding="utf-8") == "你好世界"


def test_append_non_block_raises():
    import pytest
    doc = MarkdownDocument()
    with pytest.raises(TypeError, match="Expected a Block"):
        doc.append("not a block")
