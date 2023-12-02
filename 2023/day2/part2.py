import re

file = open("input.txt", "r")

powers = 0

for line in file:
    possible = True
    line = line.strip()
    game = line.split(':')
    game_id = re.findall('Game ([0-9]+)', game[0])[0]
    sets = game[1].split(';')

    mins = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for set in sets:
        dice = set.strip().split(',')
        
        for die in dice:
            die = die.strip()
            die_values = re.fullmatch('([0-9]+) (blue|red|green)', die)
            roll_num = int(die_values[1])
            roll_color = die_values[2].strip()
            
            mins[roll_color] = max(mins[roll_color], roll_num)

    powers += mins['red']*mins['green']*mins['blue']

print(powers)