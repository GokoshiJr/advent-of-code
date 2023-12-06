import sys
from functools import reduce
D = open(sys.argv[1]).read().strip()

def find_winner(time, distance):
    result = 0
    for i in range(0, time+1):
        if i*(time-i) > distance: result += 1
    return result

times = [int(x) for x in D.split('\n')[0].split(':')[1].split(' ') if x.isdigit()]
distances = [int(x) for x in D.split('\n')[1].split(':')[1].split(' ') if x.isdigit()]

total_p1 = []
for run in range(len(times)): total_p1.append(find_winner(times[run], distances[run]))

time_p2 = int(reduce(lambda x,y: x + y, [str(x) for x in times]))
distance_p2 = int(reduce(lambda x,y: x + y, [str(x) for x in distances]))

print(reduce(lambda x, y: x * y, total_p1))
print(find_winner(time_p2, distance_p2))
