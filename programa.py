from funcoes import *
cartela = {'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1}, 'regra_avancada': {'sem_combinacao': -1, 'quadra': -1, 'full_house': -1, 'sequencia_baixa': -1, 'sequencia_alta': -1, 'cinco_iguais': -1}}
imprime_cartela (cartela)

for rodada in range(12):
    rolados = rolar_dados(5)
    guardados = []
    rerrolagens = 0
    fim_rodada = False

    while fim_rodada == False:
        print (f'Dados rolados: {rolados}')
        print (f'Dados guardados: {guardados}')
        print (f'Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')

        opcao = input()

        if opcao == '1':
            print ('Digite o índice do dado a ser guardado (0 a 4):')
            indice = int(input())
            listas = guardar_dado(rolados,guardados,indice)
            rolados = listas[0]
            guardados = listas[1]
        
        elif opcao == '2':
            print ('Digite o índice do dado a ser removido (0 a 4):')
            indice = int(input())
            listas = remover_dado(rolados,guardados,indice)
            rolados = listas[0]
            guardados = listas[1]
        
        elif opcao == '3':
            if rerrolagens >= 2:
                print ('Você já usou todas as rerrolagens.')
            else:
                rolados = rolar_dados(len(rolados))
                rerrolagens += 1
        
        elif opcao == '4':
            imprime_cartela(cartela)
        
        elif opcao == '0':
            print('Digite a combinação desejada:')
            categoria = input()

            dados = rolados + guardados
            marcou = False

            for chave in cartela['regra_simples']:
                if str(chave) == categoria:
                    marcou = True
                    if cartela['regra_simples'][chave] != -1:
                        print ('Essa combinação já foi utilizada.')
                    else:
                        faz_jogada(dados, categoria, cartela)
                        fim_rodada = True
            if marcou == False:
                if categoria in cartela ['regra_avancada']:
                    if cartela['regra_avancada'][categoria] != -1:
                        print('Essa combinação já foi utilizada.')
                    else:
                        faz_jogada(dados, categoria, cartela)
                        fim_rodada = True
                else:
                    print ('Combinação inválida. Tente novamente.')
        else:
            print ('Opção inválida. Tente novamente.')

pontuacao = 0
soma_simples = 0

for chave in cartela['regra_simples']:
    valor = cartela['regra_simples'][chave]
    pontuacao += valor
    soma_simples += valor

for chave in cartela['regra_avancada']:
    valor = cartela['regra_avancada'][chave]
    pontuacao += valor

if soma_simples >= 63:
    pontuacao += 35

imprime_cartela(cartela)
print (f'Pontuação total: {pontuacao}')
