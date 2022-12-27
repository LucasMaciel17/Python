n1 = int(input())
n2 = int(input())

if n1 > n2:
    print('Nenhuma tabuada no intervalo!')  
else:
    for i in range (n1, n2+1):
        for x in range (1,11):
            print(f'{i} x {x} = {i*x}')
        print('-' * 10)
    
