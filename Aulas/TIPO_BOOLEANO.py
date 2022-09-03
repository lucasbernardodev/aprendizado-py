# 17. O tipo booleano

# Álgebra Booleana, criada por George Boole

# 2 Constantes: True e False

# Sempre com a inicial maiúscula

ativo = False

print(ativo)

# Operaçõs básicas:

# [1] - Negação (not):

# Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
# e se for falso o resultado será verdadeiro. Ou seja, inverte o valor booleano.

print(not ativo)
# se ativo for true, not ativo será false e vice-versa

logado = False

# [2] - Ou (or):

# É uma operação binária, ou seja, depende de dois valores booleanos. Ou um ou outro
# deve ser verdadeiro.

# True or True imprime True
# True or False imprime True
# False or True imprime True
# False or False imprime False
print(ativo or logado)

# [3] - E (and):

# Também é uma operação binária, ou seja, depende de dois valores. Ambos os valores devem
# ser verdadeiros.

# True and True imprime True
# True and False imprime False
# False and True imprime False
# False and False imprime False
print(ativo and logado)