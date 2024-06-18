# semaforo-inteligente-fuzzy

## Aplicação de Lógica Nebulosa em semáforos inteligentes (Fuzzy)
O problema consiste em definir o tempo de duração de sinal verde de um tráfego local com base na densidade do tráfego em tempo real e no tempo de espera do sinal.

Entrada (antecedentes):
Densidade do Tráfego - Grau

Universo (intervalo de valores nítidos/crisp): 0 a 10

Conjunto difuso (valores difusos): baixa, média, alta

Tempo de Espera no Semáforo - Minutos

Universo (intervalo de valores nítidos/crisp): 0 a 9

Conjunto difuso (valores difusos): curto, médio, longo

Saída (consequentes):
Duração do Sinal Verde

Universo (valores nítidos/crisp): 0 a 8

Conjunto difuso (valores difusos): curto, médio, longo

Regras de Decisão
SE a densidade do tráfego é alta E o tempo de espera é longo, ENTÃO a duração do sinal verde é longa.

SE a densidade do tráfego é alta E o tempo de espera é médio, ENTÃO a duração do sinal verde é longa.

SE a densidade do tráfego é média E o tempo de espera é médio, ENTÃO a duração do sinal verde é média.

SE a densidade do tráfego é média E o tempo de espera é curto, ENTÃO a duração do sinal verde é curta.

SE a densidade do tráfego é baixa E o tempo de espera é curto, ENTÃO a duração do sinal verde é curto.
