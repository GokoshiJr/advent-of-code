f = open('txt/day1.txt', 'r')

r1 = 0
r2 = 0

for line in f:
    r1_digits = []
    r2_digits = []
    for i, letter in enumerate(line):
        if letter.isdigit():    
            r1_digits.append(letter)
            r2_digits.append(letter)
        for j, value in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(value):
                r2_digits.append(str(j+1))        
    r1 += int(r1_digits[0]+r1_digits[-1])
    r2 += int(r2_digits[0]+r2_digits[-1])
    
print(r1)      
print(r2)
