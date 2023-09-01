# Programa X v0.1

# importando libs
import time
import os
from colorama import init, Fore, Back
init(autoreset=True)

# declarando variáveis significativas
programRunning = True
nome = []
cpf = []
sangue = []
r11 = False

# começando o loop
while programRunning:
    # Menu Inicial
    print("\n Programa X \n\n 1 - Entrada de Dados \n 2 - Mostrar conjunto de dados"
          "\n 3 - Procurar no conjunto de dados \n 4 - Sair \n")

    # Tomando a escolha do usuário
    resposta1 = str(input("Digite o número da opção: "))

    # escolha 1
    if resposta1 == '1':
        # retornando a escolha do usuário e limpando a tela
        print("\nDigitado 1.")
        time.sleep(1.5)
        os.system('cls')

        # cabeçalho
        print("Inserção de Dados")

        n1 = str(input("- Digite o nome: "))
        if n1.isalpha():
            # adicionando o nome que o usuário digitou no último índice da lista
            nome.append(n1)
        else:
            print("Entrada inválida.")

        n1 = str(input("- Digite o cpf: "))
        if len(n1) == 11:
            # adicionando o cpf que o usuário digitou no último índice da lista
            cpf.append(n1)
        else:
            print("Entrada inválida.")

        n1 = str(input("- Digite o tipo sanguíneo: "))
        if len(n1) == 2:
            # adicionando o tipo sanguíneo que o usuário digitou no último índice da lista
            sangue.append(n1)
        else:
            print("Entrada inválida.")

        # atualizando o contador para marcar que já foram inseridos dados
        r11 = True

        print("Dados inseridos com sucesso!")

        # esperando interação do usuário e voltando para o menu inicial
        voltar = input("Aperte ENTER para continuar...")
        os.system('cls')

    # escolha 2 e passou pela 1
    elif resposta1 == '2' and r11:
        # retornando a escolha do usuário e limpando a tela
        print("\nDigitado 2.")
        time.sleep(1.5)
        os.system('cls')

        # cabeçalho
        print("BANCO DE DADOS \n")
        print("-" * 20)
        print("CPF      TIPO SANGUÍNEO      NOME")
        # loop para rodar (tamanho da lista nome) vezes
        for i in range(len(nome)):
            # retornando cada uma das entradas
            print(f"{cpf[i]}     {sangue[i]}     {nome[i]}")
        print("-" * 20)
        # esperando interação do usuário e voltando para o menu inicial
        voltar = input("Aperte ENTER para continuar...")
        os.system('cls')

    # escolha 3 e passou pela 1
    elif resposta1 == '3' and r11:
        # retornando a escolha do usuário e limpando a tela
        print("\nDigitado 3.")
        time.sleep(1.5)
        os.system('cls')

        # cabeçalho
        print("BUSCA NO BANCO DE DADOS")

        # recebendo o termo de busca
        busca = input("Digite o termo de busca: ")

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