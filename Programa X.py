# Programa X v5.0

# importando libs
# time serve pra esperar pra limpar a tela
import time
# os serve pra limpar a tela
import os
# colorama serve pra colorir texto
from colorama import init, Fore, Back

# settando autoreset como True pra não pintar td o texto com a msm cor dps do comando
init(autoreset=True)

# declarando variáveis significativas
# faz o programa rodar
programRunning = True
# lista pra contar
count = []
# lista pros nomes
nome = []
# lista pros cpf
cpf = []
# lista pros tipos sanguineos
sangue = []
# listas pra achar coisas no banco de dados
cpffound = []
sanguefound = []
nomefound = []
# contadores
r11 = False
n1check = False
n2check = False
right = 0
        

# list pra checar o tipo sanguineo
sangueMap = ['O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-']


def clear(timeWait):
    time.sleep(timeWait)
    os.system('cls')
    resposta1 = ""
    return resposta1


# func pra achar a string mais longa da lista (formatar o 2)
def getMax(lst):
    # quando a func é usada, o programa retorna a string mais longa da lista
    return max(lst, key=len)


# func pra fazer os cabeçalhos
def head(text, colorFore, colorBack, size):
    global cf
    global cb
    # dict pra bater as strings do argumento com os argumentos da lib
    colorForeMap = {
        'black': Fore.BLACK,
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE,
    }
    # atribuindo à var "cf" o argumento da lib
    if colorFore in colorForeMap:
        cf = colorForeMap[colorFore]

    # dict pra bater as strings do argumento com os argumentos da lib
    colorBackMap = {
        'black': Back.BLACK,
        'red': Back.RED,
        'green': Back.GREEN,
        'yellow': Back.YELLOW,
        'blue': Back.BLUE,
        'magenta': Back.MAGENTA,
        'cyan': Back.CYAN,
        'white': Back.WHITE,
    }
    # atribuindo à var "cb" o argumento da lib
    if colorBack in colorBackMap:
        cb = colorBackMap[colorBack]
    # print a linha de cima
    print(cf + cb + "".center(size))
    # print o texto centralizado na caixinha
    print(cf + cb + text.center(size))
    # print a linha de baixo
    print(cf + cb + "".center(size))
    print("")


# começando o loop
while programRunning:
    # Menu Inicial
    head("PROGRAMA X", "black", "blue", 80)
    # printando o menu inicial com o numero pintado e a opção não
    print("     " + Fore.BLACK + Back.BLUE + " 1 ", end="")
    print("    -   Adicionar à fila \n")
    print("     " + Fore.BLACK + Back.BLUE + " 2 ", end="")
    print("    -   Próximo da fila \n")
    print("     " + Fore.BLACK + Back.BLUE + " 3 ", end="")
    print("    -   Mostrar banco de dados \n")
    print("     " + Fore.BLACK + Back.BLUE + " 4 ", end="")
    print("    -   Busca no banco de dados \n")
    print("     " + Fore.BLACK + Back.BLUE + " 5 ", end="")
    print("    -   Sair \n")

    # Tomando a escolha do usuário
    resposta1 = str(input("Digite o número da opção: "))

    # escolha 1 (Inserção de Dados)
    if resposta1 == '1':
        # retornando a escolha do usuário, esperando 5s e limpando a tela
        print(Fore.LIGHTBLACK_EX + "\nDigitado 1...")
        clear(1.5)

        # cabeçalho
        head("Inserção de Dados", "black", "magenta", 80)

        # Loop até o usuário digitar um nome válido
        while not n1check:
            # tomando entrada do usuário
            n1 = str(input("- Digite o primeiro nome: "))

            # formatando n1
            n1 = n1.lower()

            # se o n1 é composto por letras
            if n1.isalpha():
                # atualizando o contador
                n1check = True

                # Loop até o usuário digitar um sobrenome válido
                while not n2check:
                    # tomando entrada do usuário
                    n2 = str(input("\n- Digite o sobrenome: "))

                    # se o n2 é composto por letras
                    if n2.isalpha():
                        # adicionando o nome que o usuário digitou no último índice da lista
                        n2 = n2.lower()

                        # n1 vira n1 com a 1a letra maiuscula, espaço, n2 com a 1a letra maiuscula
                        n1 = n1.capitalize() + " " + n2.capitalize()

                        # adicionando o n1 ao ultimo indice vazio da lista nome
                        nome.append(n1)
                        count.append(n1)

                        # atualizando o contador
                        n2check = True
                    else:
                        print("\n" + Fore.RED + "Sobrenome inválido.")
            else:
                print("\n" + Fore.RED + "Nome inválido.\n")

        # resettando os contadores
        n1check = False
        n2check = False

        # Loop até o usuário digitar um CPF válido
        while not n1check:
            # tomando entrada do usuário
            n1 = str(input("\n- Digite o cpf: "))

            # se o n1 é composto por numeros
            if n1.isnumeric():
                # add n1 no último índice da lista
                cpf.append(n1)

                # atualizando o contador
                n1check = True
            else:
                print("\n" + Fore.RED + "CPF inválido.")

        # resettando o contador
        n1check = False

        # Loop até o usuário digitar um tipo sanguineo válido
        while not n1check:
            # tomando entrada do usuário
            n1 = str(input("\n- Digite o tipo sanguíneo: "))

            # formatando n1
            n1 = n1.upper()

            # se a entrada bate com um dos tipos na lista de tipos sanguíneos
            if n1 in sangueMap:
                # atualizando o contador
                n1check = True

                # add n1 no último índice da lista
                sangue.append(n1)
            else:
                print("\n" + Fore.RED + "Tipo sanguíneo inválido.")

        # atualizando o contador para marcar que já foram inseridos dados
        r11 = True

        n1check = False
        print("")
        print(Fore.BLACK + Back.GREEN + "    Dados inseridos com sucesso!    ")

        # esperando interação do usuário e voltando para o menu inicial
        voltar = input(Fore.LIGHTBLACK_EX + "\nAperte ENTER para continuar...")
        clear(0)

    # escolha 2 (Próximo da fila)
    if resposta1 == '2':
        # retornando a escolha do usuário, esperando 5s e limpando a tela
        print(Fore.LIGHTBLACK_EX + "\nDigitado 2...")
        clear(1.5)

        # cabeçalho
        head("Próximo da Fila", "black", "magenta", 80)
        # printando 45 + (tamanho da maior string) tracinhos ("-")
        if nome:
            print("-" * (45 + len(getMax(count))))
            print("    CPF          TIPO SANGUÍNEO      NOME")
            
            # armazenando nas respectivas vars, o item indice 0 das listas
            filaCPF = cpf.pop(0)
            filaSangue = sangue.pop(0)
            filaNome = nome.pop(0)

            print(f"{filaCPF}           {filaSangue}             {filaNome}")
            # printando 45 + (tamanho da maior string) tracinhos ("-")
            print("-" * (45 + len(getMax(count))))
        else:
            print("A fila está vazia!")

        # esperando interação do usuário e voltando para o menu inicial
        voltar = input(Fore.LIGHTBLACK_EX + "\nAperte ENTER para continuar...")
        clear(0)

    # escolha 3 (Banco de Dados)
    elif resposta1 == '3':
        # retornando a escolha do usuário e limpando a tela
        print(Fore.LIGHTBLACK_EX + "\nDigitado 3...")
        clear(1.5)

        # cabeçalho
        head("Banco de Dados", "black", "magenta", 80)
        # printando 45 + (tamanho da maior string) tracinhos ("-")
        if nome:
            print("-" * (45 + len(getMax(count))))
            print("    CPF          TIPO SANGUÍNEO      NOME")

            # loop para rodar (tamanho da lista nome) vezes
            for i in range(len(cpf)):
                # retornando cada uma das entradas
                print(f"{cpf[i]}           {sangue[i]}             {nome[i]}")

            # printando 45 + (tamanho da maior string) tracinhos ("-")
            print("-" * (45 + len(getMax(count))))
        else:
            print("O banco de dados está vazio!")

        # esperando interação do usuário e voltando para o menu inicial
        voltar = input(Fore.LIGHTBLACK_EX + "\nAperte ENTER para continuar...")
        clear(0)

    # escolha 4 (Busca)
    elif resposta1 == '4':
        # retornando a escolha do usuário e limpando a tela
        print(Fore.LIGHTBLACK_EX + "\nDigitado 4...")
        clear(1.5)

        # cabeçalho
        head("Busca no Banco de Dados", "black", "magenta", 80)
        if nome:
            # recebendo o termo de busca
            busca = str(input("Digite o termo de busca: "))
            print("")

            # arrumando a busca
            # se busca não conter números, minusculo
            if not busca.isnumeric():
                busca = busca.lower()
                # se busca for nome, capitalize
                if busca in nome:
                    busca = busca.capitalize()
                # se busca for sangue, upper
                else:
                    busca = busca.upper()

            # se busca conter números (aka se busca for CPF), blz
            elif busca.isnumeric():
                pass

            # se o usuário encontrar outra opção que não: "número" ou "não número", busca inválida
            else:
                print("Busca inválida.")

            print(Fore.BLUE + "Resultados da Busca:\n")

            # loop para rodar (tamanho da lista nome) vezes
            for i in range(len(nome)):
                # checando se o termo de busca está presente em qualquer uma das listas
                if busca in cpf[i] or busca in sangue[i] or busca in nome[i]:
                    # armazenando as entradas correspondentes
                    cpffound.append(cpf[i])
                    sanguefound.append(sangue[i])
                    nomefound.append(nome[i])
                    
                    # atualizando o contador de matches
                    right += 1
            
            # se 0 matches, nn foi encontrado nada
            if right == 0:
                print(Fore.WHITE + Back.RED + "Entrada não encontrada.".center(80))
            else:
                # printando tracinho
                print("-" * (45 + len(getMax(count))))
                print("CPF            Tipo Sanguíneo     Nome")
                      
                for i in range(len(cpffound)):
                    # retornando a entrada correspondente
                    print(f"{cpffound[i]}         {sanguefound[i]}            {nomefound[i]}")
              
                # printando tracinho
                print("-" * (45 + len(getMax(count))))
        
                # resettando os parametros
                cpffound = []
                nomefound = []
                sanguefound = []
                right = 0
                
        else:
            print("O banco de dados está vazio!")
        
        # esperando interação do usuário e voltando para o menu inicial
        print("")
        voltar = input(Fore.LIGHTBLACK_EX + "Aperte ENTER para continuar...")
        clear(0)

    # escolha 5 (Encerrar)
    elif resposta1 == '5':
        # retornando a escolha do usuário e limpando a tela
        print(Fore.LIGHTBLACK_EX + "\nDigitado 5...")
        print(Fore.RED + "\nEncerrando.")
        clear(1.5)

        # interrompendo o loop
        break

    # escolha inválida
    elif resposta1 not in ["1", "2", "3", "4", "5"]:
        print(Fore.RED + "\nOpção inválida")
