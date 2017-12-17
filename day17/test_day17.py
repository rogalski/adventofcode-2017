import day17


def test_spinlock():
    s = day17.Spinlock(step_size=3)
    assert list(s.buffer) == [0]
    assert s.pointer == 0

    s.insert()
    assert list(s.buffer) == [0, 1]
    assert s.pointer == 1

    s.insert()
    assert list(s.buffer) == [0, 2, 1]
    assert s.pointer == 1

    s.insert()
    assert list(s.buffer) == [0, 2, 3, 1]
    assert s.pointer == 2


def test_spinlock_2017():
    s = day17.Spinlock(step_size=3)
    s.spin(2017)
    p_2017 = s.buffer.index(2017)
    assert s.buffer[p_2017 + 1] == 638


def test_spinlock0():
    assert day17.spinlock0(step_size=3, spin_count=1) == 1
    assert day17.spinlock0(step_size=3, spin_count=2) == 2
    assert day17.spinlock0(step_size=3, spin_count=3) == 2
