# test_jar.py

from jar import Jar
import pytest

def test_init():
    # Test default capacity
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test custom capacity
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0

    # Test invalid capacity
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("twelve")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪🍪"

def test_deposit():
    jar = Jar(3)
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(2)
    assert jar.size == 3

    # Test exceeding capacity
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    assert jar.size == 5

    jar.withdraw(3)
    assert jar.size == 2

    # Test withdrawing more than available cookies
    with pytest.raises(ValueError):
        jar.withdraw(3)

def test_capacity_and_size():
    jar = Jar(8)
    assert jar.capacity == 8
    assert jar.size == 0
    jar.deposit(4)
    assert jar.size == 4
    jar.withdraw(2)
    assert jar.size == 2
