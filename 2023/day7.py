import sys
from collections import defaultdict

D = open(sys.argv[1]).read().strip()
C = defaultdict()

total_1 = 0
total_2 = 0
labels_1 = "AKQJT98765432"
labels_2 = "AKQT98765432J"

def clasification(string, have_joker=False):
    letter_count = {}
    for letter in string:
        if letter in letter_count: letter_count[letter] += 1
        else: letter_count[letter] = 1    
    if have_joker:
        if 'J' in letter_count.keys() and not string == 'JJJJJ':
            jay_reps = letter_count['J']
            letter_count.pop('J')
            letter_count[max(letter_count, key=letter_count.get)] += jay_reps    
    if len([x for x in letter_count.items() if x[1] == 5]) == 1: return 'repoker'
    elif len([x for x in letter_count.items() if x[1] == 4]) == 1: return 'poker'
    elif len([x for x in letter_count.items() if x[1] == 3]) == 1 and len([x for x in letter_count.items() if x[1] == 2]) == 1: return 'fullhouse'
    elif len([x for x in letter_count.items() if x[1] == 3]) == 1: return 'threesome'
    elif len([x for x in letter_count.items() if x[1] == 2]) == 2: return 'two_pair'
    elif len([x for x in letter_count.items() if x[1] == 2]) == 1: return 'one_pair'
    return 'high_card'

for line in D.split('\n'): C[line.split(' ')[0]] = int(line.split(' ')[1])

high_card_1 = sorted([hand for hand in C.items() if clasification(hand[0]) == 'high_card'], key=lambda hand: [labels_1.index(card) for card in hand[0]])
high_card_2 = sorted([hand for hand in C.items() if clasification(hand[0], True) == 'high_card'], key=lambda hand: [labels_2.index(card) for card in hand[0]])

one_pair_1 = sorted([x for x in C.items() if clasification(x[0]) == 'one_pair'], key=lambda item: [labels_1.index(letra) for letra in item[0]])
one_pair_2 = sorted([x for x in C.items() if clasification(x[0], True) == 'one_pair'], key=lambda item: [labels_2.index(letra) for letra in item[0]])

two_pair_1 = sorted([x for x in C.items() if clasification(x[0]) == 'two_pair'], key=lambda item: [labels_1.index(letra) for letra in item[0]])
two_pair_2 = sorted([x for x in C.items() if clasification(x[0], True) == 'two_pair'], key=lambda item: [labels_2.index(letra) for letra in item[0]])

threesome_1 = sorted([x for x in C.items() if clasification(x[0]) == 'threesome'], key=lambda item: [labels_1.index(letra) for letra in item[0]])
threesome_2 = sorted([x for x in C.items() if clasification(x[0], True) == 'threesome'], key=lambda item: [labels_2.index(letra) for letra in item[0]])

full_house_1 = sorted([x for x in C.items() if clasification(x[0]) == 'fullhouse'], key=lambda item: [labels_1.index(letra) for letra in item[0]])
full_house_2 = sorted([x for x in C.items() if clasification(x[0], True) == 'fullhouse'], key=lambda item: [labels_2.index(letra) for letra in item[0]])

poker_1 = sorted([x for x in C.items() if clasification(x[0]) == 'poker'], key=lambda item: [labels_1.index(letra) for letra in item[0]])
poker_2 = sorted([x for x in C.items() if clasification(x[0], True) == 'poker'], key=lambda item: [labels_2.index(letra) for letra in item[0]])

repoker_1 = sorted([x for x in C.items() if clasification(x[0]) == 'repoker'], key=lambda item: [labels_1.index(letra) for letra in item[0]])
repoker_2 = sorted([x for x in C.items() if clasification(x[0], True) == 'repoker'], key=lambda item: [labels_2.index(letra) for letra in item[0]])

result_1 = repoker_1 + poker_1 + full_house_1 + threesome_1 + two_pair_1 + one_pair_1 + high_card_1
result_2 = repoker_2 + poker_2 + full_house_2 + threesome_2 + two_pair_2 + one_pair_2 + high_card_2
result_1.reverse()
result_2.reverse()

for i in range(0, len(result_1)): total_1 += (i+1) * result_1[i][1]
print(total_1)
for i in range(0, len(result_2)): total_2 += (i+1) * result_2[i][1]
print(total_2)
