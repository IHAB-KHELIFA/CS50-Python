from plates import is_valid

def test_valid_plates():
    assert is_valid("ABC123") == True
    assert is_valid("ABC23") == True
    assert is_valid("ABCD") == True
    assert is_valid("AA") == True
    assert is_valid("A99999") == False  # Too long
    assert is_valid("ABCDEF") == True

def test_invalid_start():
    assert is_valid("A1") == False
    assert is_valid("1ABC") == False
    assert is_valid("12") == False
    assert is_valid("1") == False
    assert is_valid("A") == False

def test_number_placement():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False  # Letter after number
    assert is_valid("AAA023") == False  # Zero as first number
    assert is_valid("AA02AA") == False  # Zero as first number and letters after
    assert is_valid("CS50P2") == False  # Numbers mixed with letters

def test_special_characters():
    assert is_valid("ABC,12") == False
    assert is_valid("ABC 12") == False
    assert is_valid("ABC.12") == False
    assert is_valid("ABC!12") == False
    assert is_valid("ABC-12") == False

def test_edge_cases():
    assert is_valid("") == False
    assert is_valid("A2345") == False  # Starts with one letter only
    assert is_valid("AB0123") == False  # Contains leading zero
    assert is_valid("AB12CD") == False  # Letters after numbers
    assert is_valid("AB12.3") == False  # Contains period
