"""
A simple calculator language, this doesn't implement precedence, just uses
reverse polish notation like old calculators did. For example you would write
"1 + 2" as

    > 1 2 +
    3

And you write "(1 + 2) * 3" as

    > 1 2 + 3 *
    9

Compare it with "1 + (2 * 3)" which is

    > 1 2 3 * +
    7
"""


def tokenize(input: str) -> list[str]:
    raise NotImplementedError()


def evaluate(input: str) -> list[str]:
    raise NotImplementedError()
