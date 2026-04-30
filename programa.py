from funcoes import *

cartela = {'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1}, 'regra_avancada': {'sem_combinacao': -1, 'quadra': -1, 'full_house': -1, 'sequencia_baixa': -1, 'sequencia_alta': -1, 'cinco_iguais': -1}}

imprime_cartela(cartela)

for rodada in range(12):
    guardados = []
    rolados = rolar_dados(5)
    rerrolagens = 0
    mostrar_menu = True

    fim_rodada = False
    while fim_rodada == False:
        if mostrar_menu == True:
            print(f'Dados rolados: {rolados}')
            print(f'Dados guardados: {guardados}')
        print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
        mostrar_menu = True
        opcao = input()

        if opcao == '1':
            print('Digite o índice do dado a ser guardado (0 a 4):')
            indice = int(input())
            if 0 <= indice < len(rolados):
                listas = guardar_dado(rolados, guardados, indice)
                rolados = listas[0]
                guardados = listas[1]

        elif opcao == '2':
            print('Digite o índice do dado a ser removido (0 a 4):')
            indice = int(input())
            if 0 <= indice < len(guardados):
                listas = remover_dado(rolados, guardados, indice)
                rolados = listas[0]
                guardados = listas[1]

        elif opcao == '3':
            if rerrolagens >= 2:
                print('Você já usou todas as rerrolagens.')
            else:
                rolados = rolar_dados(len(rolados))
                rerrolagens += 1

        elif opcao == '4':
            imprime_cartela(cartela)

        elif opcao == '0':
            print('Digite a combinação desejada:')
            marcou_jogada = False
            while marcou_jogada == False:
                categoria = input()
                if categoria in ['1', '2', '3', '4', '5', '6']:
                    if cartela['regra_simples'][int(categoria)] != -1:
                        print('Essa combinação já foi utilizada.')
                    else:
                        faz_jogada(rolados + guardados, categoria, cartela)
                        marcou_jogada = True
                        fim_rodada = True
                elif categoria in cartela['regra_avancada']:
                    if cartela['regra_avancada'][categoria] != -1:
                        print('Essa combinação já foi utilizada.')
                    else:
                        faz_jogada(rolados + guardados, categoria, cartela)
                        marcou_jogada = True
                        fim_rodada = True
                else:
                    print('Combinação inválida. Tente novamente.')

        else:
            print('Opção inválida. Tente novamente.')
            mostrar_menu = False

pontuacao = 0
soma_simples = 0

for chave in cartela['regra_simples']:
    valor = cartela['regra_simples'][chave]
    if valor != -1:
        pontuacao += valor
        soma_simples += valor

for chave in cartela['regra_avancada']:
    valor = cartela['regra_avancada'][chave]
    if valor != -1:
        pontuacao += valor

if soma_simples >= 63:
    pontuacao += 35

imprime_cartela(cartela)
print(f'Pontuação total: {pontuacao}')