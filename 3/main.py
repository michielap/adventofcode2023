import numpy as np
import re

data = np.loadtxt('input.txt', dtype=str, delimiter=',', comments=None)
data = np.insert(data, 0, 140*'.')
data = np.append(data, 140*'.')

total = 0

for i in range(len(data)):

    if i == len(data)-1 or i == 0:
        continue

    row = data[i]
    row_prev = data[i-1]
    row_next = data[i+1]

    res = re.compile(r'\d+')
    for match in res.finditer(row):

        include = False
        start = match.start()
        end = match.end()

        if start == 0:
            subtract = 0
        else:
            subtract = 1

        if end == len(row):
            add = 0
        else:
            add = 1

        if bool(re.search(r'[@$*+/#%=&-]', row[start-subtract:end+add])):
            include = True

        if bool(re.search(r'[@$*+/#%=&-]', row_prev[start-subtract:end+add])):
            include = True

        if bool(re.search(r'[@$*+/#%=&-]', row_next[start-subtract:end+add])):
            include = True
        
        if include:
            total = total + int(row[start:end])

print(total)