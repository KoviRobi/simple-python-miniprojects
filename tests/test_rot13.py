from rot13 import rot13

def test_hello_world_simple():
    assert rot13("helloworld") == "uryybjbeyq"

def test_hello_world_spaces():
    assert rot13("hello world") == "uryyb jbeyq"

def test_hello_world_complex():
    assert rot13("Hello, world!") == "Uryyb, jbeyq!"
