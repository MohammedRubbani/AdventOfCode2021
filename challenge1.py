def read_file(filename):
    with open(filename) as f:
        return f.read().splitlines()


def main():
    file = read_file("AoC_day1Input.txt")
    print(file)


if __name__ == '__main__':
    main()

