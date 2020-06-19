import csv
from random import randint

nummer = ['1', '2', '3', '4']

tilfældig = randint(0, 3)

antal = 0

tom = []

forsøg = 7

with open('tilfældige_ord.csv', 'r') as words:
    reader = csv.reader(words, delimiter = ";")
    next(words)
    for row in reader:
        if row[1] == nummer[tilfældig]:
            word = row[0]
            letters = []
            for i in word:
                antal += 1
                letters.append(i)
    # streger = [i for i in range(antal)]
    # for i in streger:
    #     f = '_'
    #     tom.append(f)
        

running = True

while running:

    forsøg -= 1

    print(f'{forsøg} tilbage')

    msg = input('Say a letter> ')

    tallet = 0

    for i in letters:
        tallet += 1
        if i == msg:
            forsøg += 1
            antal -= 1
            print(f'Bogstavet {msg} indgår i ordet og har plads nummer {tallet}')
            print(f'Der er {antal} ord tilbage')

    print(f'Ordet du skal finde er {antal} bogstaver')

    if antal == 0:
        print("Du gættede hele ordet inden for 6 forsøg!")
        running = False

    if forsøg == 0:
        running = False