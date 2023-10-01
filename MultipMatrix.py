# -*- coding: utf-8 -*-

import time
import matplotlib.pyplot as plt
import numpy as np



# implementação do algoritmo usando listas

def Mmult(M1,M2):
    if len(M1[0]) != len(M2):
        print("Inválido.")
    M3 = []
    for i in range(0,len(M1)):
        linha_i=[]
        for j in range(len(M2[0])):
            somatorio = 0
            for k in range(len(M1[i])):
                somatorio = somatorio + M1[i][k] * M2[k][j]
            linha_i.append(somatorio)
        M3.append(linha_i)
    return M3



# implementação do algoritmo usando arrays numpy
def multiplica_matriz_numpy(M1, M2):
    
    return np.matmul( np.array(M1), np.array(M2))



# implementacao do experimento
def experimento(funcao, N):

    resultado_listas = list() # lista vazia, para resultados
    valores_n = range(1, N, 2) # sequencia de valores
    
    for n_i in valores_n:
    
        horario_inicio = round(time.time() * 1000)
    
        m1 = [list(range(n_i))]*n_i
        m2 = [list(range(n_i))]*n_i
    
        output = funcao(m1, m2) # executando função iterativa
    
        horario_fim = round(time.time() * 1000)
        tempo_gasto = horario_fim - horario_inicio
    
        print('\nn =', n_i)
        print('horario_inicio:', horario_inicio)
        print('horario_fim:', horario_fim)
        print('Tempo:', tempo_gasto, 'milissegundos')
        
        resultado_listas.append(tempo_gasto)
    
    return valores_n, resultado_listas



# rodando o experimento
valores_n, resultado_listas = experimento(Mmult, 100)
valores_n, resultado_numpy = experimento(multiplica_matriz_numpy, 100)



# analisando os resultados
plt.scatter(valores_n, resultado_listas)
plt.scatter(valores_n, resultado_numpy)
plt.ylabel('Tempo (ms)')
plt.xlabel('N (dimensão da matriz)')
plt.legend(['Algoritmo com listas', 'Algoritmo com numpy'])
plt.show()