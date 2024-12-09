from twttr import shorten

def test_shorten_with_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"

def test_shorten_with_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"

def test_shorten_with_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("HeLLo") == "HLL"

def test_shorten_with_numbers():
    assert shorten("h3ll0") == "h3ll0"
    assert shorten("1234") == "1234"

def test_shorten_with_punctuation():
    assert shorten("hello!") == "hll!"
    assert shorten("hi.there") == "h.thr"

def test_shorten_with_empty_string():
    assert shorten("") == ""
