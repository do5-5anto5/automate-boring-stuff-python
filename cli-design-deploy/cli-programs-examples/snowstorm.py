import  subprocess, time, random, sys

TOP= chr(9600)
BOTTOM = chr(9604)
FULL = chr(9608)

DENSITY = 10 # Default snow density = 4%

if len(sys.argv) > 1:
    DENSITY = sys.argv[1]

def clear():
    subprocess.run(['cls'], shell=True)

while True:
    clear()

    for x in range(20):
        for y in range(40):
            # print snow flakes, or empty spaces
            if random.randint(0,99) < DENSITY:
                print(random.choice([TOP, BOTTOM]), end='')
            else:
                print(' ', end='')

        print()
    print(FULL * 40 + '\n' + FULL * 40)
    print('CTRL + C to stop')
    time.sleep(2)
