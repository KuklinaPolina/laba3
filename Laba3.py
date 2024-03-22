def b():
    n = 1000000
    z = 1
    c = []
    while z <= n:
        s = str(input("Bbedute clovo: "))
        if s == "stop":
            break
        c.append(s)
    v = " ".join(c)
    print(v)
def a():
    n = int(input("Bbedute koluchectbo clob, kotopoe xotute zapucat: "))
    z = 1
    c = []
    while z <= n:
        s = str(input("Bbedute clovo: "))
        c.append(s)
        z += 1
    v = " ".join(c)
    print(v)
def c():
    x = 1
    while x <= 5:
        f = 0
        s = str(input("Bbedute clobo: "))
        for y in s:
            if y == "ф":
                print("Ogo! Eto pegkoe clobo! ")
                x += 1
        if f == 0:
            print("Ex, eto ne ochen pegkoe clobo...")
def d():
    import random
    o = 0
    b = 0
    while o < 3:
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        r = x + y
        v = int(input("{} + {} = ".format(x, y)))
        if v != r:
            print("Otbet neberno!")
            o += 1
        else:
            print("Prabulno!")
            b += 1
    print("Ugra okonchena. Prabelnux otbetob: ", b)