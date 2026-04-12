from markdownpal.blocks.table import TableBlock


def test_table_basic():
    block = TableBlock(
        headers=["Name", "Age"],
        rows=[["Alice", "30"], ["Bob", "25"]]
    )
    expected = (
        "| Name | Age |\n"
        "| --- | --- |\n"
        "| Alice | 30 |\n"
        "| Bob | 25 |"
    )
    assert block.render() == expected


def test_table_single_row():
    block = TableBlock(headers=["Key", "Value"], rows=[["foo", "bar"]])
    expected = "| Key | Value |\n| --- | --- |\n| foo | bar |"
    assert block.render() == expected


def test_table_three_columns():
    block = TableBlock(
        headers=["A", "B", "C"],
        rows=[["1", "2", "3"]]
    )
    expected = "| A | B | C |\n| --- | --- | --- |\n| 1 | 2 | 3 |"
    assert block.render() == expected
