from random import randint

tilfældig = randint(0, 20)

running = True

while running:

    msg = int(input(f'Gæt tallet (hint: Det er mellem 0 og 20) > '))

    if 0 > msg or 20 < msg:
        print(f'\nDu skal gætte på et tal mellem 0 og 20! Dit gæt var {msg}\n')

    elif msg > tilfældig:
        print(f'\nDit gæt på tallet {msg} var for højt\n')

    elif msg < tilfældig:
        print(f'\nDit gæt på tallet {msg} var for lavt\n')

    elif msg == tilfældig:
        print(f'\nDit gæt var rigtigt! \nNu er der oprettet et nyt tal\n')
        tilfældig = randint(0, 20)