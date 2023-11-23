class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def get_first(self):
        return self.first

    def get_second(self):
        return self.second

    def __str__(self):
        return f"Pair{{first={self.first}, second={self.second}}}"
