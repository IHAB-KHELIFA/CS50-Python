from um import count

def test_single_um():
    assert count("hello, um, world") == 1

def test_multiple_ums():
    assert count("um, hello, um, goodbye") == 2

def test_case_insensitivity():
    assert count("UM, um, Um, uM") == 4

def test_not_a_substring():
    assert count("yummy umbrella") == 0

def test_with_punctuation():
    assert count("Um... did you say 'um'?") == 2

def test_no_um():
    assert count("hello world") == 0
