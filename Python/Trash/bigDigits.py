Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ",
           "** ",
           " * ",
           " * ",
           " * ",
           "***"]
Two = [" *** ", "*   *", "   * ", "  *  ", " *   ", "*****"]
Digits = [Zero, One, Two]

try:
    digits = input("Input number: ")
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            for c in digit[row]:
                if c == "*":
                    c = str(number)
                line += c
            line += "  "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)