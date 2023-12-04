import numpy as np
import re

data = np.loadtxt('input.txt', dtype=str, delimiter=':')
max_card = len(data)

total = 0
for row in data:
    print()
    row_id  = row[0].replace('Card ', '')

    drawn, winning = row[1].split('|')
    drawn = re.findall(r'\d+', drawn)
    winning = re.findall(r'\d+', winning)

    intersect = np.intersect1d(drawn, winning)
    n_matches = len(intersect)
    
    score = 0
    if n_matches > 0:
        score = 2 ** (n_matches - 1)



    total = total + score
print(total)


global count
count = 0

def score(data, id):

    global count
    count = count + 1

    row = data[id]

    drawn, winning = row[1].split('|')
    drawn = re.findall(r'\d+', drawn)
    winning = re.findall(r'\d+', winning)
    
    n_matches = len(np.intersect1d(drawn, winning))
    

    for i in np.arange(1,n_matches+1):
        if id+i <= max_card:
            score(data, id+i)
        else:
            print("Reached max card")

for i in np.arange(0, len(data)):
    print(i)
    score(data, i)