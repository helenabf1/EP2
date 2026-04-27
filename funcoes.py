import random
def rolar_dados (n):
    nova = []
    i = 0
    while i<n:
        valor = 0
        valor = random.randint(1,6)
        nova.append(valor)
        i += 1
    return nova
