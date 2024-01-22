symbol = "$"

def line_width(width):
    return f"{width * symbol}"

print(line_width(10))
print()


def line_heigh(heigh):
    for i in range(heigh):
        print(symbol)      

line_heigh(5)
print()