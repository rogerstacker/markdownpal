from markdownpal.blocks.list_ import ULBlock, OLBlock, TaskListBlock


def test_ul_block():
    block = ULBlock(["apple", "banana", "cherry"])
    assert block.render() == "- apple\n- banana\n- cherry"


def test_ul_single_item():
    assert ULBlock(["only"]).render() == "- only"


def test_ol_block():
    block = OLBlock(["first", "second", "third"])
    assert block.render() == "1. first\n2. second\n3. third"


def test_ol_single_item():
    assert OLBlock(["one"]).render() == "1. one"


def test_task_list_mixed():
    block = TaskListBlock([("done task", True), ("pending task", False)])
    assert block.render() == "- [x] done task\n- [ ] pending task"


def test_task_list_all_done():
    block = TaskListBlock([("a", True), ("b", True)])
    assert block.render() == "- [x] a\n- [x] b"
