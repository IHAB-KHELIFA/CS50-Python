from bank import value

def test_hello_greetings():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0
    assert value("Hello, Newman") == 0
    assert value("HELLO, friend") == 0

def test_h_greetings():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("HI THERE") == 20
    assert value("How are you?") == 20
    assert value("Hi, friend!") == 20

def test_other_greetings():
    assert value("good morning") == 100
    assert value("what's up") == 100
    assert value("yo") == 100
    assert value("WELCOME") == 100
    assert value("1234") == 100

def test_edge_cases():
    assert value("HELLO!!!!") == 0
    assert value("hELLo WoRLD") == 0
    assert value("hi!!!") == 20
    assert value("h") == 20
    assert value("") == 100
