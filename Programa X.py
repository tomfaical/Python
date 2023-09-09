# Programa X v1.0

# importando libs
# time serve pra esperar pra limpar a tela
import time
# os serve pra limpar a tela
import os
# colorama serve pra colorir texto
import colorama
from colorama import init, Fore, Back
colorama.init()
# settando autoreset como True pra não pintar td o texto com a msm cor dps do comando
init(autoreset=True)

# declarando variáveis significativas
# faz o programa rodar
programRunning = True
# lista pros nomes
nome = []
# lista pros cpf
cpf = []
# lista pros tipos sanguineos
sangue = []
# contadores
r11 = False
n1check = False
n2check = False

# começando o loop
while programRunning:
    # Menu Inicial
    print(Back.MAGENTA + Fore.BLACK + 'Programa X'.center(40))
    
    print(Fore.GREEN + '1- Entrada de Dados'.center(30))
    
    print(Fore.GREEN + '2- Mostrar conjunto de dados '.center(40))
    
    print(Fore.GREEN + '3- Procurar no conjunto de dados '.center(40))
    
    print(Fore.GREEN + '4- Sair'.center(30))
          
    
    # Tomando a escolha do usuário
    resposta1 = str(input("Digite o número da opção: "))

    # escolha 1
    if resposta1 == '1':
        # retornando a escolha do usuário, esperando 5s e limpando a tela
        print("\nDigitado 1.")
        time.sleep(1.5)
        os.system('cls')

        # cabeçalho
        print(Back.MAGENTA + Fore.BLACK + "Inserção de Dados".center(40))

        n1 = str(input(Fore.GREEN + "- Digite o primeiro nome: "))
        # Loop até o usuário digitar um nome válido
        while not n1check:
            # formatando n1
            n1 = n1.lower()
            # atualizando o contador
            n1check = True
            # se o n1 é composto por letras
            if n1.isalpha():
                # Loop até o usuário digitar um sobrenome válido
                while not n2check:
                    n2 = str(input(Fore.GREEN + "- Digite o sobrenome: "))
                    # se o n2 é composto por letras
                    if n2.isalpha():
                        # adicionando o nome que o usuário digitou no último índice da lista
                        n2 = n2.lower()
                        # n1 vira n1 com a 1a letra maiuscula, espaço, n2 com a 1a letra maiuscula
                        n1 = n1.capitalize() + " " + n2.capitalize()
                        # adicionando o n1 ao ultimo indice vazio da lista nome
                        nome.append(n1)
                        # atualizando o contador
                        n2check = True
                    else:
                        print("Entrada inválida.")
            else:
                print("Entrada inválida.")

        n1 = str(input(Fore.GREEN + "- Digite o cpf: "))
        # Loop até o usuário digitar um CPF válido
        while not n1check:
            # se o n1 é composto por numeros
            if n1.isnumeric():
                # add n1 no último índice da lista
                cpf.append(n1)
                #atualizando o contador
                n1check = True
            else:
                print("Entrada inválida.")

        n1 = str(input(Fore.GREEN + "- Digite o tipo sanguíneo: "))

        while not n1check:
        # Loop até o usuário digitar um tipo sanguineo válido
            # se n1 for letra ou numero
            if n1.isalnum():
                # formatando n1
                n1 = n1.upper()
                # add n1 no último índice da lista
                sangue.append(n1)
                #atualizando o contador
                n1check = True
            else:
                print("Entrada inválida.")

        # atualizando o contador para marcar que já foram inseridos dados
        r11 = True

        print(Fore.GREEN + "Dados inseridos com sucesso!")

        # esperando interação do usuário e voltando para o menu inicial
        voltar = input(Fore.GREEN + "Aperte ENTER para continuar...")
        os.system('cls')

    # escolha 2 e passou pela 1
    elif resposta1 == '2' and r11:
        # retornando a escolha do usuário e limpando a tela
        print("\nDigitado 2.")
        time.sleep(1.5)
        os.system('cls')

        # cabeçalho
        print(Back.MAGENTA + Fore.BLACK +"BANCO DE DADOS \n".center(40))
        print("-" * 20)
        print(Fore.GREEN + "CPF      TIPO SANGUÍNEO      NOME")
        # loop para rodar (tamanho da lista nome) vezes
        for i in range(len(nome)):
            # retornando cada uma das entradas
            print(f"{cpf[i]}     {sangue[i]}     {nome[i]}")
        print("-" * 20)
        # esperando interação do usuário e voltando para o menu inicial
        voltar = input(Fore.GREEN + "Aperte ENTER para continuar...")
        os.system('cls')

    # escolha 3 e passou pela 1
    elif resposta1 == '3' and r11:
        # retornando a escolha do usuário e limpando a tela
        print("\nDigitado 3.")
        time.sleep(1.5)
        os.system('cls')

        # cabeçalho
        print(Back.MAGENTA + Fore.BLACK + "BUSCA NO BANCO DE DADOS".center(40))

        # recebendo o termo de busca
        busca = str(input(Fore.GREEN + "Digite o termo de busca: "))

        # arrumando a busca
        # se busca não conter números (aka se busca for nome ou tipo sanguíneo), formatar
        if not busca.isnumeric():
            busca = busca.lower()
            busca = busca.capitalize()

        # se busca conter números (aka se busca for CPF), blz
        elif busca.isnumeric():
            pass

        # se o usuário encontrar outra opção que não "número" ou "não número", busca inválida
        else:
            print("Busca inválida.")

        # loop para rodar (tamanho da lista nome) vezes
        for i in range(len(nome)):
            # checando se o termo de busca está presente em qualquer uma das listas
            if busca in cpf[i] or busca in sangue[i] or busca in nome[i]:
                # retornando a entrada correspondente
                print(f"{cpf[i]}     {sangue[i]}     {nome[i]}")

        # esperando interação do usuário e voltando para o menu inicial
        voltar = input("Aperte ENTER para continuar...")
        os.system('cls')

    # escolha 4
    elif resposta1 == '4':
        # retornando a escolha do usuário e limpando a tela
        print("\nDigitado 4. \n\nEncerrando...")
        time.sleep(1.5)
        os.system('cls')

        # interrompendo o loop
        break

    # escolha inválida
    else:
        print("\nOpção inválida")
