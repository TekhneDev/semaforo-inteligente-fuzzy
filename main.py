import numpy as np # type: ignore
import skfuzzy as fuzz # type: ignore
from skfuzzy import control as ctrl # type: ignore
#import matplotlib.pyplot as plt


# Cria as variáveis do problema
densidadeTrafego = ctrl.Antecedent(np.arange(0, 11, 1), 'Densidade Trafego (Grau)') # Grau de 0 a 10
tempoEsperaSemaforo = ctrl.Antecedent(np.arange(0, 10, 1), 'Tempo Espera Semaforo (Minutos)') # Duracao tempo de espera no semaforo de 0 a 9 minutos
duracaoSinalVerde = ctrl.Consequent(np.arange(0, 9, 1), 'Duracao Sinal Verde (Minutos)') # Duracao do sinal no verde de 0 a 8 minutos


#################################
# Cria as funções de pertinência
densidadeTrafego['baixa'] = fuzz.trimf(densidadeTrafego.universe, [0, 0, 3])
densidadeTrafego['média'] = fuzz.trimf(densidadeTrafego.universe, [2, 4, 7])
densidadeTrafego['alta'] = fuzz.trimf(densidadeTrafego.universe, [6, 8, 10]) #mudar cor de alto para vermelho no grafico

tempoEsperaSemaforo['curto'] = fuzz.trimf(tempoEsperaSemaforo.universe, [0, 0, 3])
tempoEsperaSemaforo['médio'] = fuzz.trimf(tempoEsperaSemaforo.universe, [2, 4, 6])
tempoEsperaSemaforo['longo'] = fuzz.trimf(tempoEsperaSemaforo.universe, [5, 7, 9]) #mudar cor de alto para vermelho no grafico

duracaoSinalVerde['curto'] = fuzz.trapmf(duracaoSinalVerde.universe, [0, 0, 1, 2])
duracaoSinalVerde['médio'] = fuzz.trapmf(duracaoSinalVerde.universe, [1, 2, 4, 5])
duracaoSinalVerde['longo'] = fuzz.trapmf(duracaoSinalVerde.universe, [3, 5, 6, 8]) #mudar cor de alto para vermelho no grafico
####################################

"""
densidadeTrafego.view()
tempoEsperaSemaforo.view()
duracaoSinalVerde.view()

input()
"""

####################################
# Criando regras difusas
rule1 = ctrl.Rule(densidadeTrafego['alta'] & tempoEsperaSemaforo['longo'], duracaoSinalVerde['longo'])
rule2 = ctrl.Rule(densidadeTrafego['alta'] & tempoEsperaSemaforo['médio'], duracaoSinalVerde['longo'])
rule3 = ctrl.Rule(densidadeTrafego['média'] & tempoEsperaSemaforo['médio'], duracaoSinalVerde['médio'])
rule4 = ctrl.Rule(densidadeTrafego['média'] & tempoEsperaSemaforo['curto'], duracaoSinalVerde['curto'])
rule5 = ctrl.Rule(densidadeTrafego['baixa'] & tempoEsperaSemaforo['curto'], duracaoSinalVerde['curto'])

# rule2.view()
#####################################


#####################################
# Criando e simulando o controlador Fuzzy
duracaoSinalVerde_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
duracaoSinalVerde_simulador = ctrl.ControlSystemSimulation(duracaoSinalVerde_ctrl)

# teste - print(densidadeTrafego)

# Entrando com valores para a densidade do tráfego local e o tempo de espera no semáforo
duracaoSinalVerde_simulador.input['Densidade Trafego (Grau)'] = 8
duracaoSinalVerde_simulador.input['Tempo Espera Semaforo (Minutos)'] = 7

# Computando o resultado
duracaoSinalVerde_simulador.compute()
# teste - print(duracaoSinalVerde_simulador.output['Duracao Sinal Verde (Minutos)'])
#####################################


# Mostrando graficamente o resultado final
densidadeTrafego.view(sim=duracaoSinalVerde_simulador)
tempoEsperaSemaforo.view(sim=duracaoSinalVerde_simulador)
duracaoSinalVerde.view(sim=duracaoSinalVerde_simulador)