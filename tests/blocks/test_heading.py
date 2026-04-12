from markdownpal.blocks.heading import H1Block, H2Block, H3Block, H4Block, H5Block, H6Block


def test_h1():
    assert H1Block("Title").render() == "# Title"


def test_h2():
    assert H2Block("Section").render() == "## Section"


def test_h3():
    assert H3Block("Sub").render() == "### Sub"


def test_h4():
    assert H4Block("Detail").render() == "#### Detail"


def test_h5():
    assert H5Block("Minor").render() == "##### Minor"


def test_h6():
    assert H6Block("Tiny").render() == "###### Tiny"


def test_h1_with_inline_markup():
    assert H1Block("**Bold Title**").render() == "# **Bold Title**"
