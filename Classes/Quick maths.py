import Maths as m

while True:
    try:
        msg = input("\nHvad vil du beregne?: ")
        if msg.startswith('trekant'):
            b = msg.split(' ')
            h = int(b[1])
            g = int(b[2])
            a = m.trekant.areal(g, h)
            print(a)
        if msg == "q":
            break
    except Exception as e:
        print(e)
        print("[ERROR] Error in the program, fix it!")
print("Bye")