import time
andarAtual = 0
andarDestino = 0
andarMaximo = 2
andarMinimo = 0
portaAberta = True

while True:
    print(f'Elevador no andar: {andarAtual}\n')
    andarDestino = int(input(f'Digite o andar desejado (0, 1, 2) ou -1 para sair: '))
    portaAberta = False

    if (andarDestino == -1):
        print(f'=============================')
        print('Porta abrindo...')
        time.sleep(3)
        portaAberta = True
        print('Porta aberta')
        break

    elif (andarDestino < 0 or andarDestino > 2):
        print("Andar inválido! Tente novamente.")

    else:

        while(andarAtual != andarDestino):

            if(andarDestino > andarAtual):
                if ((andarAtual + 2) == andarDestino):
                    print(f'=============================')
                    portaAberta = False
                    print('Fechando as portas...')
                    time.sleep(3)
                    print('Portas fechadas.')
                print('Subindo...')
                time.sleep(5)
                andarAtual = andarAtual + 1

            elif (andarDestino < andarAtual):
                print(f'=============================')
                if ((andarAtual - 2) == andarDestino):
                    print(f'=============================')
                    portaAberta = False
                    print('Fechando as portas...')
                    time.sleep(3)
                    print('Portas fechadas.')
                print('Descendo...')
                time.sleep(5)
                andarAtual = andarAtual - 1

            print(f'=============================')

            print(f'Chegamos ao andar: {andarAtual}')

        print(f'Abrindo portas no andar: {andarAtual}')
        print(f'Portas abertas.')
        portaAberta = True

        print('Elevador desligado.')
            


        
