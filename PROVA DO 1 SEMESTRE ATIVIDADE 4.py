def troca(s, i, j):
    a[i], s[j] = s[j], s[i]

def empurra_minimo(s, n):
    for i in range(n-1):
        if s[i] < s[i+1]:
            troca(s, i, i+1)

def empurra_maximo(s, n):
    for i in range(n-1):
        if s[i] > s[i+1]:
            troca(s, i, i+1)

def buble_sort(s, crestente=False):
    n = len(s)

    if crescente:
        empurra = empurra_maximo
    else:
        empurra = empurra_minimo

    while n > 1:
        empurra(s, n)
        n -= 1
            
