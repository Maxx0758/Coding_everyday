import random
import string

def random_password(antal):
    '''
    Skal modtage antal fra input af brugeren.
    '''
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(antal))

running = True
while running:
    msg = input(f'Hvor langt skal dit password være?> ')

    if msg.isdigit():
        
        if int(msg) < 6:
            print("Kodeordet skal være mindst 6 tegn")

        elif int(msg) >= 6:
            password = random_password(int(msg))
            print(f'Dit nye kodeord er: {password}')
    
    else:
        if msg == 'Quit':
            running = False
