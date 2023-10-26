"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(num=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Initialize SerialGenerator and define starting point"""
        self.start = self.num2 = start

    def generate(self):
        "Adds 1 to current number; -1 prevents skipping initial starting point"
        self.num2 += 1
        return self.num2 - 1

    def reset(self):
        """Resets increased number back to original"""
        self.num2 = self.start
