from morse import decode, encode

def test_sos_encode():
    assert encode("sos") == "... --- ..."

def test_sos_decode():
    assert decode("... --- ...") == "sos"

def test_words_encode():
    assert encode("hi rob") == ".... ..   .-. --- -..."

def test_words_decode():
    assert encode( ".... ..   .-. --- -...") =="hi rob"
