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

def calcula_pontos_regra_simples (lista):
    novo = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for num in lista:
        novo[num] += num
    return novo
        
def calcula_pontos_soma (lista):
    total = 0
    for n in lista:
        total = total + n
    return total

def calcula_pontos_sequencia_baixa(lista):
    if 1 in lista and 2 in lista and 3 in lista and 4 in lista:
        return 15
    if 2 in lista and 3 in lista and 4 in lista and 5 in lista:
        return 15
    if 3 in lista and 4 in lista and 5 in lista and 6 in lista:
        return 15
    return 0

def calcula_pontos_sequencia_alta (lista):
    if 1 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista:
        return 30
    elif 2 in lista and 3 in lista and 4 in lista and 5 in lista and 6 in lista:
        return 30
    return 0