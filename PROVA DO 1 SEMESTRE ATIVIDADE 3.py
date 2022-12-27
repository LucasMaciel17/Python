def misterio1():
    x = 0
    while True:
        y = int(input('valor: '))
        if y < 0: break
        x += y
    return x

def misterio2():
    x = 0
    while True:
        y = int(input('valor: '))
        if y < 0: continue
        x += y
    return x

