import re

def get_ranges(destination, source, num_range):
    ranges = {}
    for i in range(num_range):
        ranges[source+i] = destination+i
    return ranges

def get_map(lines):
    map = {}
    for line in lines:
        line = line.strip()
        if line == '':
            continue

        parts = line.split(' ')
        destination = int(parts[0])
        source = int(parts[1])
        num_range = int(parts[2])

        map.update(get_ranges(destination, source, num_range))
    return map

file = open("input.txt", "r")

section = {}
section_index = 0

for line in file:
    line = line.strip()
    if line == '':
        section_index += 1
        continue
    
    if section_index not in section:
        section[section_index] = []

    section[section_index].append(line)

seed_to_soil_map = get_map(section[1][1:])
soil_to_fertilizer_map = get_map(section[2][1:])
fertilizer_to_water_map = get_map(section[3][1:])
water_to_light_map = get_map(section[4][1:])
light_to_temperature_map = get_map(section[5][1:])
temperature_to_humidity_map = get_map(section[6][1:])
humidity_to_location_map = get_map(section[7][1:])


seeds = [ int(x) for x in re.findall('[0-9]+',section[0][0])]

min_location = None

for seed in seeds:
    soil = seed_to_soil_map[seed] if seed in seed_to_soil_map else seed
    fertilizer = soil_to_fertilizer_map[soil] if soil in soil_to_fertilizer_map else soil
    water = fertilizer_to_water_map[fertilizer] if fertilizer in fertilizer_to_water_map else fertilizer
    light = water_to_light_map[water] if water in water_to_light_map else water
    temperature = light_to_temperature_map[light] if light in light_to_temperature_map else light
    humidity = temperature_to_humidity_map[temperature] if temperature in temperature_to_humidity_map else temperature
    location = humidity_to_location_map[humidity] if humidity in humidity_to_location_map else humidity

    min_location = min(min_location, location) if min_location is not None else location

print(min_location)