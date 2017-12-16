import day16


def test_shift_1():
    positions = list("abcde")
    day16.shift(positions, 1)
    assert positions == list("eabcd")


def test_shift_2():
    positions = list("abcde")
    day16.shift(positions, 2)
    assert positions == list("deabc")


def test_swap_by_index():
    positions = list("eabcd")
    day16.swap_by_index(positions, 3, 4)
    assert positions == list("eabdc")


def test_swap_by_value():
    positions = list("eabdc")
    day16.swap_by_value(positions, "e", "b")
    assert positions == list("baedc")
