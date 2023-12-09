import sys
D = open(sys.argv[1]).read().strip()
all_arr = []
acum = 0
acum_2 = 0
for line in D.split('\n'):
    all_arr = [] 
    arr = [int(number) for number in line.split(' ')]
    while not (all(x == 0 for x in arr)):
        all_arr.append(arr)
        arr_last = arr
        arr = []
        for i in range(len(arr_last)-1): arr.append(arr_last[i+1]-arr_last[i])
        if (all(x == 0 for x in arr)): all_arr.append(arr)
    all_arr.reverse()
    num = 0 # part 1
    for i in range(len(all_arr)-1):
        num += all_arr[i+1][len(all_arr[i+1])-1]
        if i == len(all_arr)-2: acum += num
    num = 0 # part 2
    for j in range(len(all_arr)-1):
        num = -num+all_arr[j+1][0]
        if j == len(all_arr)-2: acum_2 += num
print(acum)
print(acum_2)
