import math
from random import randint

listofnumbers = []

for i in range(10):
    i = randint(1, 100)
    listofnumbers.append(i)

listofnumbers.sort()


'''
Funktion der bliver ved med at dele listen op, for at checke hvilken side tallet befinder sig i (hvis det gør).
'''

def findnumber(number):
    global listofnumbers
    left, right = (0, len(listofnumbers))
    middle = (left + right)//2

    '''
    Et eller andet med at tage fra midten og til left af list og numbers, derefter gøre det samme for midten til højre.
    '''

    if len(listofnumbers) == 1:
        if number == listofnumbers[0]:
            print("Tallet er det samme som dit gæt!")
        else:
            print("Tallet var ikke en del af listen")

    elif number < listofnumbers[middle]:
        print("Er mindre end den miderste værdi")
        listofnumbers = listofnumbers[left:middle]

    elif number >= listofnumbers[middle]:
        print("Er større end den miderste værdi")
        listofnumbers = listofnumbers[middle:right]



running = True

while running:

    msg = int(input("Choose a number (1, 100 and only ints) > "))

    findnumber(msg)

