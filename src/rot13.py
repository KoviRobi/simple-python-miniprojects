"""
Implement ROT13, a common (old-fashioned) internet "cipher" used as avoiding
spoilers rather than any security benefit. It is a Caesar cipher, shifts each
letter 13 places (chosen because there are 26 letters in the English alphabet,
so encoding and decoding are the same operations).

E.g. "abc" would get turned into "nop". See also `tests/test_rot13.py`
"""


def rot13(text: str) -> str:
    raise NotImplementedError()
