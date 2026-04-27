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

def guardar_dado (rolados, guardados, num):
    listafinal = []
    guardados.append(rolados[num])
    del rolados[num]
    listafinal.append(rolados)
    listafinal.append(guardados)
    return listafinal

def remover_dado (rolados, estoque, n):
    nova = []
    rolados.append(estoque[n])
    del estoque[n]
    nova.append(rolados)
    nova.append(estoque)
    return nova


