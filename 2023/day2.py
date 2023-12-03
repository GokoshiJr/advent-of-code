import re, sys
D = open(sys.argv[1]).read().strip()
result_1 = 0
result_2 = 0
red = 0
green = 0
blue = 0
for line in D.split('\n'):
    ok = True
    red_array = []
    green_array = []
    blue_array = []
    for e in [x.split(';') for x in line.split(':')][1]:
        for cube in [x.lstrip() for x in e.split(',')]:
            if re.search('red', cube): 
                red = int(''.join([x for x in cube if x.isdigit()]))            
                red_array.append(red)
            if re.search('green', cube): 
                green = int(''.join([x for x in cube if x.isdigit()]))
                green_array.append(green)
            if re.search('blue', cube):
                blue = int(''.join([x for x in cube if x.isdigit()]))
                blue_array.append(blue)
            if (red > 12): ok = False
            if (green > 13): ok = False
            if (blue > 14): ok = False            
        red = 0
        green = 0
        blue = 0
    result_2 += max(red_array) * max(green_array) * max(blue_array)
    if ok: result_1 += int([x.split(';') for x in line.split(':')][0][0].strip('Game').lstrip())
print(result_1)
print(result_2)
