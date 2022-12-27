c = input()
p = int(input())
if c =='domingo':
    c = 1
elif c =='segunda':
    c = 2
elif c =='terca':
    c = 3
elif c =='quarta':
    c = 4
elif c =='quinta':
    c = 5
elif c =='sexta':
    c = 6
elif c =='sabado':
    c = 7
    
if (c + p > 7):
    e = c + p - 7
elif:
    e = c + p
    
if p == 0:
    print('chegara hoje!')
elif e == 1:
    print('sera entregue domingo')
elif e == 2:
    print('sera entregue segunda')
elif e == 3:
    print('sera entregue terca')
elif e == 4:
    print('sera entregue quarta')
elif e == 5:
    print('sera entregue quinta')
elif e == 6:
    print('sera entregue sexta')
elif e == 7:
    print('sera entregue sabado')

