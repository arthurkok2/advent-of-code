import re
import functools 
file = open("input.txt", "r")

sum = 0

for line in file:
    winning_set = set()
    score = 0
    sections = line.strip().split('|')
    [ winning_set.add(x) for x in re.findall('[0-9]+', sections[0].split(':')[1])]
    
    for have_number in re.findall('[0-9]+', sections[1]):
        if have_number in winning_set:
            score += 1
    
    if score > 0:
        sum += 2**(score-1)
    
print(sum)