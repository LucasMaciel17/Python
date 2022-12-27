n = int(input('Insira um numero para gerar a sequência de Fibonnaci: '))

t1 = 0

t2 = 1

cont = 1

while cont <= n:

   t3 = t1 + t2

   print(',{}'.format(t3), end = '')

   t1 = t2

   t2 = t3

   cont += 1

