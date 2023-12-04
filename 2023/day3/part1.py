import re

file = open("input.txt", "r")

class Number:
    col1: int
    col2: int
    row: int
    value: int

    def __init__(self, col1, col2, row, value):
        self.col1 = col1
        self.col2 = col2
        self.row = row
        self.value = value

    def __repr__(self):
        return '%d @ (%d,%d)(%d,%d)' % (self.value, self.row, self.col1, self.row, self.col2)

    def is_part_number(self, map: list[str]):
        is_part = False
        for col in range(self.col1-1, self.col2+2):
            for row in range(self.row-1, self.row+2):
                
                if col < 0 or row < 0 or row >= len(map) or col >= len(map[row]):
                    continue

                if col >= self.col1 and col <= self.col2 and row == self.row:
                    continue

                if map[row][col] != '.':
                    is_part = True

        return is_part       

numbers : list[Number] = []
map: list[str] = []

line_index = 0
for line in file:
    map.append(line.strip())

    for m in re.finditer('([0-9]+)', line):
        numbers.append(Number(m.start(), m.end()-1, line_index, int(m.group(0))))

    line_index += 1

sum = 0

for number in numbers:
    if number.is_part_number(map):
        sum += number.value

print(sum)
        