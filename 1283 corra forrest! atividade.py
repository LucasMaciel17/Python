tempos = []
soma = 0
qtd = 0

tempo = int(input())

while tempo >= 0:
    tempos.append(tempo)
    soma += tempo
    qtd += 1
    tempo = int(input())
media = soma / qtd
print(f'MÉDIA: {media:.2f}')    

for i in range (len(tempos)):
        if tempos[i] < media:
                print(tempos[i])
