n1 = int(input())
n2 = int(input())

cont = 0
x = n1
while x < n2:
    if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        print(x)
        cont += 1
      
print(f'bissextos: {cont}')



# metodo do professor com for
def bissexto(ano):
    return (ano % 4 == 0 and ano % 100 !=0) or ano % 400 ==0

inicio = int(input())
fim = int(input())
qtd_bissextos = 0

for ano in range(inicio, fim+1):
    if bissexto(ano):
        print(ano)
        qtd_bissextos += 1

print(f'bissextos: {qtd_bissextos}')


# metodo do professor com while
def bissexto(ano):
    return (ano % 4 == 0 and ano % 100 !=0) or ano % 400 ==0

inicio = int(input())
fim = int(input())
qtd_bissextos = 0
ano = inicio

while ano <= fim:
    if bissexto(ano):
        print(ano)
        qtd_bissextos += 1
        ano += 1

print(f'bissextos: {qtd_bissextos}')

