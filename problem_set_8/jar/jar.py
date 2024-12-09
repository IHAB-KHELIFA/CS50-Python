# jar.py

class Jar:
    def __init__(self, capacity=12):
        # Check that capacity is a non-negative integer
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        # Return 🍪 symbols representing the number of cookies
        return "🍪" * self._cookies

    def deposit(self, n):
        # Check if adding n cookies exceeds the jar's capacity
        if self._cookies + n > self._capacity:
            raise ValueError("Not enough capacity for that many cookies.")
        self._cookies += n

    def withdraw(self, n):
        # Check if there are enough cookies to withdraw n
        if n > self._cookies:
            raise ValueError("Not enough cookies to withdraw.")
        self._cookies -= n

    @property
    def capacity(self):
        # Return the jar's capacity
        return self._capacity

    @property
    def size(self):
        # Return the current number of cookies
        return self._cookies
