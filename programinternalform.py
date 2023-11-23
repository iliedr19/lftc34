class ProgramInternalForm:
    def __init__(self):
        self.token_position_pair = []
        self.types = []

    def add(self, pair, _type):
        self.token_position_pair.append(pair)
        self.types.append(_type)

    def __str__(self):
        computed_string = ""
        for i, item in enumerate(self.token_position_pair):
            computed_string += f"{item.get_first()} - {item.get_second()} -> {self.types[i]}\n"
        return computed_string
