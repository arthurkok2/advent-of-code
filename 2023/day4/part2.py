import re
import functools 
file = open("input.txt", "r")

sum = 0

# read example2.txt to the end
lines = file.readlines()

# define an array to hold the scores
cards = [1] * len(lines)
score_map = {}

def get_score(line):
    winning_set = set()
    score = 0
    sections = line.strip().split('|')
    [ winning_set.add(x) for x in re.findall('[0-9]+', sections[0].split(':')[1])]

    for have_number in re.findall('[0-9]+', sections[1]):
        if have_number in winning_set:
            score += 1

    return score

def win(id, cards):
    if id not in score_map:
        score_map[id] = get_score(lines[id])
    
    score = score_map[id]

    if score == 0:
        return
    else:
        for i in range(1, score+1):
            if id+i < len(lines):
                cards[id+i] += 1
                win(id+i, cards)
            

for i in range(len(lines)):
    win(i, cards)
    
print(functools.reduce(lambda a, b: a + b, cards))



    
