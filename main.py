from myscanner import MyScanner


def print_to_file(file_path, obj):
    with open(file_path, 'w') as file:
        file.write(str(obj))


def run(file_path):
    scanner = MyScanner(file_path)
    scanner.scan()
    print_to_file(file_path.replace(".txt", "ST.txt"), scanner.get_symbol_table())
    print_to_file(file_path.replace(".txt", "PIF.txt"), scanner.get_pif())


if __name__ == "__main__":
    run("p1.txt")
    run("p2.txt")
    run("p3.txt")
    run("p1err.txt")
