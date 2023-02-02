"""
Implement a morse-code decoder, that operates on a space-separated morse code,
like so, for SOS

    ... --- ...

Here is the morse code for reference

 	A   .-
 	B   -...
 	C   -.-.
 	D   -..
 	E   .
 	F   ..-.
 	G   --.
 	H   ....
 	I   ..
 	J   .---
 	K
 	L   .-..
 	M   --
 	N   -.
 	O   ---
 	P   .--.
 	Q   --.-
 	R   .-.
 	S   ...
 	T   -
 	U   ..-
 	V   ...-
 	W   .--
 	X   -..-
 	Y   -.--
 	Z   --..
"""


def encode(text: str) -> str:
    """
    Turn normal text into morse code.
    """
    raise NotImplementedError()


def decode(text: str) -> str:
    """
    Turn morse code into normal text.
    """
    raise NotImplementedError()
