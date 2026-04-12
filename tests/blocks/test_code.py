from markdownpal.blocks.code import CodeBlock


def test_code_block_with_lang():
    block = CodeBlock("print('hi')", lang="python")
    assert block.render() == "```python\nprint('hi')\n```"


def test_code_block_no_lang():
    block = CodeBlock("x = 1")
    assert block.render() == "```\nx = 1\n```"


def test_code_block_multiline():
    code = "def foo():\n    return 42"
    block = CodeBlock(code, lang="python")
    assert block.render() == "```python\ndef foo():\n    return 42\n```"
