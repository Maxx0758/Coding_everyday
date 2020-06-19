from random import randint

tilfældig = randint(0, 20)

running = True

while running:

    msg = input(f'Gæt tallet (hint: Det er mellem 0 og 20) > ')

    if 0 > int(msg) or 20 < int(msg):
        print(f'Du skal gætte på et tal mellem 0 og 20! Dit gæt var {msg}')

    elif int(msg) > tilfældig:
        print(f'Dit gæt på tallet {msg} var for højt')

    elif int(msg) < tilfældig:
        print(f'Dit gæt på tallet {msg} var for lavt')

    elif int(msg) == tilfældig:
        print(f'Dit gæt var rigtigt! \nNu er der oprettet et nyt tal')
        tilfældig = randint(0, 20)