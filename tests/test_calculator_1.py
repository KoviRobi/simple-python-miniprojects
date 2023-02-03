from calculator_1 import tokenize, evaluate


def test_tokenize():
    assert tokenize("1 2 +") == ["1", "2", "+"]


def test_evaluate_1():
    assert evaluate("1 2 +") == 3


def test_evaluate_2():
    assert evaluate("1 2 + 3 *") == 9


def test_evaluate_3():
    assert evaluate("1 2 3 * +") == 9
