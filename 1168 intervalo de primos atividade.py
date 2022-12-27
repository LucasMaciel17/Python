def primo(n):
    qtd_divisores = 0
    for divisor in range(1, n+1):
        if n % divisor == 0:
            qtd_divisores +=1
    return qtd_divisores == 2

inicio = int(input())
fim = int(input())
qtd_primos = 0

for n in range(inicio, fim+1):
    if primo(n):
        qtd_primos += 1
        print(n)

print(f'primos: {qtd_primos}')

