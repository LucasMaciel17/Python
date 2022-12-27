cont = 0
soma = 0
while True:
    valor = float(input())
    if valor < 0:
        break
    cont += 1
    soma += valor
total = soma * 2.50
print(f'VC$ {soma:.2f}')
print(f'R$ {total:.2f}')




# metedo do professor de resolver 
# total_vic = 0.0
# vic_coin = float(input())

# while vic_coin != -1.0:
   # total_vic += vic_coin
  #  vic_coin = float(input())

 # total_reais = total_vic * 2.50
 # print(f'VC$ {total_vic:.2f}')
# print(f'R$ {total_reais:.2f}')
