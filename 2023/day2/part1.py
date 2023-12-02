import re

file = open("input.txt", "r")

max = {
    'red': 12,
    'green': 13,
    'blue': 14
}

possible_num = 0

for line in file:
    possible = True
    line = line.strip()
    game = line.split(':')
    game_id = re.findall('Game ([0-9]+)', game[0])[0]
    sets = game[1].split(';')

    for set in sets:
        dice = set.strip().split(',')
        
        for die in dice:
            die = die.strip()
            die_value = re.fullmatch('([0-9]+) (blue|red|green)', die)
            
            if int(die_value[1]) > max[die_value[2].strip()]:
                possible = False
                break;

        if not possible:
            break;

    
    if possible:
        print(game_id)
        possible_num += int(game_id)

print('Total impossible games: ' + str(possible_num))