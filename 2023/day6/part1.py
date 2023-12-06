import re

lines = open("input.txt", "r").readlines()

times = re.findall('[0-9]+', lines[0])
distances = re.findall('[0-9]+', lines[1])

time_distance = list(zip(times, distances))

def get_time_over_distance(time, distance):
    times_over_distance = 0
    for i in range(time):
        speed = i
        new_distance = speed * (time-i)
        if new_distance > distance:
            times_over_distance += 1
    return times_over_distance

win_times = 1

for tuple in time_distance:
    win_times *= get_time_over_distance(int(tuple[0]), int(tuple[1]))

print(win_times)