import re
from multiprocessing import Pool

def get_map(lines):
    map = []
    for line in lines:
        line = line.strip()
        if line == '':
            continue

        parts = line.split(' ')
        destination = int(parts[0])
        source = int(parts[1])
        num_range = int(parts[2])

        map.append({
            'destination': destination,
            'source': source,
            'num_range': num_range
        })

    return map

def find_destination(source, map):
    for item in map:
        if source >= item['source'] and source <= item['source'] + item['num_range']:
            return item['destination'] + (source - item['source'])
    return source

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

def source_range_to_dest_range(start_source, num_range, map, indent='\t'):
    new_ranges = []
    print(f'{indent}start_source: {start_source}, num_range: {num_range}')
    for item in map:
        if start_source >= item['source'] and start_source < item['source'] + item['num_range']:
            print(f'{indent}Found item: {item}')
            max_input_source = start_source + num_range + 1
            max_item_source = item['source'] + item['num_range']
            print(f'{indent}Max input source: {max_input_source}')
            print(f"{indent}Max item source: {max_item_source}")
            
            if max_input_source > max_item_source:
                print(f'{indent}Max input source is greater than max item source')
                print(f'{indent}Splitting original range into two')
                range_one = { 'start': start_source, 'num_range': max_item_source-start_source }
                range_two = { 'start': start_source+(max_item_source-start_source), 'num_range': max_input_source-(start_source+(max_item_source-start_source+1)) }
                print(indent,range_one, range_two)
                destination_start = item['destination'] + (range_one['start'] - item['source'])
                destination_end = destination_start + range_one['num_range']
                print(f'{indent}Destination start: {destination_start}, destination end: {destination_end}')
                new_ranges.append({ 'start': destination_start, 'num_range': destination_end-destination_start })
                new_ranges.extend(source_range_to_dest_range(range_two['start'], range_two['num_range'], map, indent+'\t'))
                return new_ranges
            else:
                destination_start = item['destination'] + (start_source - item['source'])
                destination_end = destination_start + num_range
                new_ranges.append({ 'start': destination_start, 'num_range': destination_end-destination_start })
                return new_ranges

    print(f'{indent}No item found, returning original range')
    new_ranges.append({ 'start': start_source, 'num_range': num_range })
    return new_ranges

min_location = None

for i in range(int(len(seeds)/2)):
    print()
    start_seed = seeds[i*2]
    num_range = seeds[i*2+1]
    print(f'start_seed: {start_seed}, num_range: {num_range}')

    soil_ranges = source_range_to_dest_range(start_seed, num_range, seed_to_soil_map)
    print(f'soil_ranges: {soil_ranges}')

    fertilizer_ranges = []

    for soil_range in soil_ranges:
        fertilizer_ranges.extend(source_range_to_dest_range(soil_range['start'], soil_range['num_range'], soil_to_fertilizer_map))

    print(f'fertilizer_ranges: {fertilizer_ranges}')

    water_ranges = []
    for fertilizer_range in fertilizer_ranges:
        water_ranges.extend(source_range_to_dest_range(fertilizer_range['start'], fertilizer_range['num_range'], fertilizer_to_water_map))

    print(f'water_ranges: {water_ranges}')

    light_ranges = []
    for water_range in water_ranges:
        light_ranges.extend(source_range_to_dest_range(water_range['start'], water_range['num_range'], water_to_light_map))

    print(f'light_ranges: {light_ranges}')

    temperature_ranges = []
    for light_range in light_ranges:
        temperature_ranges.extend(source_range_to_dest_range(light_range['start'], light_range['num_range'], light_to_temperature_map))

    print(f'temperature_ranges: {temperature_ranges}')

    humidity_ranges = []
    for temperature_range in temperature_ranges:
        humidity_ranges.extend(source_range_to_dest_range(temperature_range['start'], temperature_range['num_range'], temperature_to_humidity_map))

    print(f'humidity_ranges: {humidity_ranges}')

    location_ranges = []
    for humidity_range in humidity_ranges:
        location_ranges.extend(source_range_to_dest_range(humidity_range['start'], humidity_range['num_range'], humidity_to_location_map))

    print(f'location_ranges: {location_ranges}')

    for location_range in location_ranges:
        if min_location is None or location_range['start'] < min_location:
            min_location = location_range['start']

print(min_location)