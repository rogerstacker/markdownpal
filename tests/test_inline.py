from markdownpal.inline import bold, italic, code, strikethrough


def test_bold():
    assert bold("hello") == "**hello**"


def test_italic():
    assert italic("hello") == "*hello*"


def test_code():
    assert code("x = 1") == "`x = 1`"


def test_strikethrough():
    assert strikethrough("old") == "~~old~~"


def test_bold_empty_string():
    assert bold("") == "****"


def test_composable():
    assert bold(italic("text")) == "***text***"
