
file = open("input.txt", "r")

calibration = 0
lookup = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9,
    'zero' : 0
}

def checkEndsWith(line):
    for key in lookup:
        if line.endswith(key):
            return lookup[key]
    return None

def checkStartsWith(line):
    for key in lookup:
        if line.startswith(key):
            return lookup[key]
    return None

# loop each line
for line in file:
    line = line.strip()
    first = ''
    last = ''
    current = ''
    
    for i in range(0, len(line)):
        if line[i].isdigit():            
            first = line[i]
            break
        else:
            current = current + line[i]
            check_num = checkEndsWith(current)
            if check_num is not None:
                first = str(check_num)
                break

    current = ''

    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():            
            last = line[i]
            break
        else:
            current = line[i] + current
            check_num = checkStartsWith(current)
            if check_num is not None:
                last = str(check_num)     
                break

    calibration += int(first + last)
    print(line)
    print(first + last)
    assert(len(first+last) == 2)
    
print(calibration)