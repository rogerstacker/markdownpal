from markdownpal.blocks.text import TextBlock, QuoteBlock, HRBlock, CommentBlock


def test_text_block():
    assert TextBlock("Hello world").render() == "Hello world"


def test_text_block_with_inline():
    assert TextBlock("Say **hi** now").render() == "Say **hi** now"


def test_quote_block():
    assert QuoteBlock("A wise quote").render() == "> A wise quote"


def test_hr_block():
    assert HRBlock().render() == "---"


def test_comment_block():
    assert CommentBlock("This is a note").render() == "<!-- This is a note -->"
