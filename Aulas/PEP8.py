# 10. PEP8 - Boas Práticas

# [1] - Utilizar CamelCase para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

# [2] - Utilizar nomes em minúsculo, separados por underline para funções ou variáveis;

def soma():
    pass


def soma_dois():
    pass

numero = 4

numero_impar = 5

# [3] - Utilizar 4 espaços para identação!

if 'a' in 'banana':
    print('tem')

# [4] - Linhas em branco

class Classe:
    pass


class ClassDois:
    pass

# Separar funções e definições de classe com duas linhas em branco;
# Métodos dentro de uma classe devem ser separados com uma única linha em branco;

# [5] - Imports de pacotes completos devem ser sempre feitos em linhas separadas;

# -- Errado

import sys, os

# -- Certo

import sys
import os

# -- Não há problemas em utilizar quando importar itens de um pacote

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comen
# tários ou docstrings e antes de constantes ou variáveis globais.
    
# [6] - Espaços em expressões e instruções

# -- Não faça:

funcao( algo[ 1 ], { outro: 2 } )

algo (1)

dict ['chave'] = lista [indice]

x              = 1
y              = 3
variavel_longa = 5

# -- Faça:

funcao(algo[1], {outro:2})

algo(1)

dict['chave'] = lista[indice]

x = 1
y = 3
variavel_longa = 5

# [7] - Terminar sempre uma instrução com uma nova linha

import this
