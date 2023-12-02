import numpy as np

# 12 red cubes, 13 green cubes, and 14 blue cubes
max_red = 12
max_green = 13
max_blue = 14

input_data = np.loadtxt('input.txt', dtype=str, delimiter=':')
total = 0
total_power = 0

for row in input_data:
    id = int(row[0].replace('Game ', ''))
    data = row[1]
    include_set = True
    print(data)

    min_red = 0
    min_blue = 0
    min_green = 0

    for set in data.split(';'):
        for grab in set.split(','):
            
            if "red" in grab:
                color = 'red'
                cnt = int(grab.replace(' red', ''))
                min_red = cnt if min_red < cnt else min_red
            elif "blue" in grab:
                color = 'blue'
                cnt = int(grab.replace(' blue', ''))
                min_blue = cnt if min_blue < cnt else min_blue
            elif "green" in grab:
                color = 'green'
                cnt = int(grab.replace(' green', ''))
                min_green = cnt if min_green < cnt else min_green
            
            if color == 'red' and cnt>max_red:
                include_set = False
            elif color == 'blue' and cnt>max_blue:
                include_set = False
            elif color == 'green' and cnt>max_green:
                include_set = False

    if include_set:
        total = total + id
    total_power = total_power + min_red * min_blue * min_green

print(total)
print(total_power)