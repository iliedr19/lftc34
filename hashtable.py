from pair import Pair


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def find_by_pos(self, pos):
        if len(self.table) <= pos.get_first() or len(self.table[pos.get_first()]) <= pos.get_second():
            raise IndexError("Invalid position")
        return self.table[pos.get_first()][pos.get_second()]

    def get_size(self):
        return self.size

    def find_position_of_term(self, elem):
        pos = self.hash(elem)
        if self.table[pos]:
            elems = self.table[pos]
            for i, e in enumerate(elems):
                if e == elem:
                    return Pair(pos, i)
        return None

    def hash(self, key):
        sum_chars = sum(ord(c) for c in key)
        return sum_chars % self.size

    def contains_term(self, elem):
        return self.find_position_of_term(elem) is not None

    def add(self, elem):
        if self.contains_term(elem):
            return False
        pos = self.hash(elem)
        self.table[pos].append(elem)
        return True

    def __str__(self):
        computed_string = ""
        for i, item in enumerate(self.table):
            if item:
                computed_string += f"{i} - {item}\n"
        return computed_string
