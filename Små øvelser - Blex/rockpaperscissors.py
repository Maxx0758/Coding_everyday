import random

computerslag = ['Sten', 'Saks', 'Papir']

running = True

while running:
    
    msg = input('Sten, Saks eller Papir?> ')

    k = random.choice(computerslag)

    if msg == 'Sten':

        if k == 'Sten':
            print("\nComputeren valgte sten")
            print('Uafgjort\n')

        elif k == 'Saks':
            print("\nComputeren valgte saks")
            print('Spiller vandt\n')

        elif k == 'Papir':
            print("\nComputeren valgte papir")
            print('Computer vandt\n')

    elif msg == 'Saks':

        if k == 'Sten':
            print("\nComputeren valgte sten")
            print('Computer vandt\n')

        elif k == 'Saks':
            print("\nComputeren valgte saks")
            print('Uafgjort\n')
            
        elif k == 'Papir':
            print("\nComputeren valgte papir")
            print('Spiller vandt\n')

    elif msg == 'Papir':

        if k == 'Sten':
            print("\nComputeren valgte sten")
            print('Spiller vandt\n')

        elif k == 'Saks':
            print("\nComputeren valgte saks")
            print('Computer vandt\n')
            
        elif k == 'Papir':
            print("\nComputeren valgte papir")
            print('Uafgjort\n')
            