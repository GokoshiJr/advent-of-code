import sys
D = open(sys.argv[1]).read().strip()

def find_minor(value, matrix):
    for e in matrix:
        destiny, origin, r = e
        if origin <= value < origin + r:
            value = destiny + (value-origin)   
            break
    return value

seeds = []
map = []
matrix = []
for line in D.split('\n'):
    if 'seeds:' in line: seeds = [int(x) for x in line.strip('seeds: ').split(' ')]
    if len(line):
        if line[0].isdigit(): map.append([int(x) for x in line.split(' ')])
    else:
        matrix.append(map)
        map = []
matrix.append(map)    
matrix.pop(0)
value = 0
ubications = []   
for seed in seeds:    
    value = seed
    for l in matrix:        
        value = find_minor(value, l)
    ubications.append(value)
print(min(ubications))
         