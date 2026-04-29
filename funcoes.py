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

def calcula_pontos_full_house (lista):
    valores = []
    for num in lista:
        if num not in valores:
            valores.append(num)
    if len(valores) != 2:
        return 0
    count1 = 0
    count2 = 0
    for num in lista:
        if num == valores[0]:
            count1 += 1
        else:
            count2 += 1
    if count1 == 3 and count2 == 2 or count1 == 2 and count2 == 3:
        soma = 0
        for num in lista:
            soma += num
        return soma
    return 0

def calcula_pontos_quadra(lista):
    for numero in lista:
        count = 0
        for numero2 in lista:
            if numero == numero2:
                count = count + 1
        if count >= 4:
            total = 0
            for valor in lista:
                total = total + valor
            return total
    return 0

def calcula_pontos_quina (lista):
    for num in lista:
        count = 0

        for n in lista:
            if n == num:
                count += 1
        if count >= 5:
            return 50
    return 0

def calcula_pontos_regra_avancada (lista):
    pontos = {}

    pontos['cinco_iguais'] = calcula_pontos_quina(lista)
    pontos['full_house'] = calcula_pontos_full_house(lista)
    pontos['quadra'] = calcula_pontos_quadra(lista)
    pontos['sem_combinacao'] = calcula_pontos_soma(lista)
    pontos['sequencia_alta'] = calcula_pontos_sequencia_alta(lista)
    pontos['sequencia_baixa'] = calcula_pontos_sequencia_baixa (lista)

    return pontos

def faz_jogada (dados, categoria, cartela):
    if categoria in cartela['regra_simples']:
        cartela['regra_simples'][categoria] = calcula_pontos_regra_simples(dados)[categoria]
    else:
        if categoria in cartela['regra_avancada']:
            cartela['regra_avancada'][categoria] = calcula_pontos_regra_avancada(dados)[categoria]
    return cartela