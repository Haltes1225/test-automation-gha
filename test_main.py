from main import factorials


def test_factorials_1():
    expected = [1]
    assert list(factorials(1)) == expected


def test_factorials_5():
    expected = [1, 2, 6, 24, 120]
    assert list(factorials(5)) == expected


def test_factorials_0():
    expected = []
    assert list(factorials(0)) == expected


def test_factorials_minus_1():
    expected = []
    assert list(factorials(-1)) == expected


def test_factorials_string_type_error():
    try:
        f = factorials("a")
        next(f)
        assert False, "Type error expected"
    except TypeError:
        pass


def test_factorials_list_type_error():
    try:
        f = factorials([])
        next(f)
        assert False, "Type error expected"
    except TypeError:
        pass


def test_factorials_fraction_type_error():
    try:
        f = factorials(0.5)
        next(f)
        assert False, "Type error expected"
    except TypeError:
        pass


def test_factorials_stop_iteration():
    try:
        f = factorials(1)
        next(f)
        next(f)
        assert False, "StopIteration error expected"
    except StopIteration:
        pass

def test_factorials_dummy():
    assert False