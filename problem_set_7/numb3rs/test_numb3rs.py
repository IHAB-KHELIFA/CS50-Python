import numb3rs

def test_valid_addresses():
    assert numb3rs.validate("192.168.1.1") == True
    assert numb3rs.validate("0.0.0.0") == True
    assert numb3rs.validate("255.255.255.255") == True
    assert numb3rs.validate("127.0.0.1") == True

def test_invalid_addresses():
    assert numb3rs.validate("275.3.6.28") == False
    assert numb3rs.validate("256.256.256.256") == False
    assert numb3rs.validate("192.168.1.256") == False
    assert numb3rs.validate("192.168@1.1") == False
    assert numb3rs.validate("192.168.1.1.1") == False
    assert numb3rs.validate("192.168.1") == False
