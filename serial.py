"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

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
        self.start = self.next_num = start

    def __repr__(self):
        """Show representation."""
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Generates the next int after start and continues until reset"""
        self.next_num += 1
        return self.next_num -1

    def reset(self):
        """resets back to start int"""
        self.next_num = self.start



