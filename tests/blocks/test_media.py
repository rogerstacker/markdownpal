from markdownpal.blocks.media import ImageBlock, LinkBlock


def test_image_with_alt():
    assert ImageBlock(src="logo.png", alt="Logo").render() == "![Logo](logo.png)"


def test_image_no_alt():
    assert ImageBlock(src="photo.jpg").render() == "![](photo.jpg)"


def test_link():
    assert LinkBlock(text="Click here", url="https://example.com").render() == "[Click here](https://example.com)"


def test_link_with_chinese():
    assert LinkBlock(text="点击这里", url="https://example.com").render() == "[点击这里](https://example.com)"
