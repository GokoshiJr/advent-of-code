import sys
D = open(sys.argv[1]).read().strip()
acum = 0
for line in D.split('\n'):
    card = line.split(':')[0]
    winners = [x for x in line.split(':')[1].split('|')[0].split(' ') if x != '']
    attempts = [x for x in line.split(':')[1].split('|')[1].split(' ') if x != '']
    count = 0
    for e in attempts:
        if e in winners: count += 1
    result = 0
    if count >= 2: 
        result = 1
        for i in range(count-1):
            result *= 2
    elif count == 1: result = 1
    acum += result
print(acum)
