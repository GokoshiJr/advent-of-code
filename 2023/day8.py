import sys
from collections import defaultdict
from math import lcm

D = open(sys.argv[1]).read().strip()
C = defaultdict()
coords = D.split('\n')[0]

for line in D.split('\n')[2:]: C[line.split('=')[0].strip(' ')] = (''.join(filter(lambda x: x.isalpha() or x.isnumeric(), line.split('=')[1].split(',')[0])), ''.join(filter(lambda x: x.isalpha() or x.isnumeric(), line.split('=')[1].split(',')[1])))

position = 'AAA'
count = 0
salir = False
while not (salir):
    for coord in coords:
        if coord == 'R': position = C[position][1]
        elif coord == 'L': position = C[position][0]
        count += 1
        if position == 'ZZZ':
            salir = True
            break
print(count)

result = []
for position in [key for key in C.keys() if key[2] == 'A']:
    salir = False
    count = 0
    while not (salir):
        for coord in coords:
            if coord == 'R': position = C[position][1]
            elif coord == 'L': position = C[position][0]
            count += 1
            if position.endswith('Z'):
                salir = True
                result.append(count)
                break
print(lcm(*result))
