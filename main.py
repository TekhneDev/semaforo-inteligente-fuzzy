import numpy as np # type: ignore
import skfuzzy as fuzz # type: ignore
from skfuzzy import control as ctrl # type: ignore
#import matplotlib.pyplot as plt


# Cria as variáveis do problema
densidadeTrafego = ctrl.Antecedent(np.arange(0, 11, 1), 'Densidade Trafego Grau') # Grau de 0 a 10
tempoEsperaSemaforo = ctrl.Antecedent(np.arange(0, 10, 1), 'Tempo Espera Semaforo em Minutos') # Duracao tempo de espera no semaforo de 0 a 9 minutos
duracaoSinalVerde = ctrl.Consequent(np.arange(0, 9, 1), 'Duracao Sinal Verde em Minutos') # Duracao do sinal no verde de 0 a 8 minutos


# Criar as funções de pertinência
densidadeTrafego['baixa'] = fuzz.trimf(densidadeTrafego.universe, [0, 0, 3])
densidadeTrafego['média'] = fuzz.trimf(densidadeTrafego.universe, [2, 4, 7])
densidadeTrafego['alta'] = fuzz.trimf(densidadeTrafego.universe, [6, 8, 10]) #mudar cor de alto para vermelho no grafico

tempoEsperaSemaforo['baixo'] = fuzz.trimf(tempoEsperaSemaforo.universe, [0, 0, 3])
tempoEsperaSemaforo['médio'] = fuzz.trimf(tempoEsperaSemaforo.universe, [2, 4, 6])
tempoEsperaSemaforo['alto'] = fuzz.trimf(tempoEsperaSemaforo.universe, [5, 7, 9]) #mudar cor de alto para vermelho no grafico

duracaoSinalVerde['baixa'] = fuzz.trapmf(duracaoSinalVerde.universe, [float(0), float(0), float(1), float(2)])
duracaoSinalVerde['média'] = fuzz.trapmf(duracaoSinalVerde.universe, [1, 2, 4, 5])
duracaoSinalVerde['alta'] = fuzz.trapmf(duracaoSinalVerde.universe, [3, 5, 6, 8]) #mudar cor de alto para vermelho no grafico

densidadeTrafego.view()
tempoEsperaSemaforo.view()
duracaoSinalVerde.view()

input()

