# 12. Recebendo dados de usuário

# input() -> Todo dado recebido via input é do tipo String

# Em Python, string é tudo que estiver entre:
# - Aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
# - Aspas duplas -> "uma string", "234", "a", "True", "42.3"
# - Aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
# - Aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

# Entrada de dados
# print('Qual é o seu nome?')
# nome = input()  # Input -> Entrada

nome = input('Qual é o seu nome? ')

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

# print('Qual é a sua idade?')
# idade = input()

idade = int(input('Qual é a sua idade? '))

# Processamento

# Saída de dados
# Exemplo de print 'antigo' 2.x
# print('%s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('{0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'{nome} tem {idade} anos')

# int(idade) => cast

# Cast é a 'conversão' de um tipo de dado para outro

# print(f'{nome} nasceu em {2022 - int(idade)}')

print(f'{nome} nasceu em {2022 - idade}')
