from number_parse import parse


def test_parse_1():
    assert parse("456") == 456


def test_parse_2():
    assert parse("123456789") == 123456789
