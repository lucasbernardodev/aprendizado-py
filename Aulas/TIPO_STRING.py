# 18. O tipo string

# Em Python, uma string é uma sequência de caracteres. Ou seja, uma cadeia de
# caracteres entre àspas simples, duplas, simples triplas e duplas triplas.

nome = 'Lucas Gabriel'
print(nome[0:5]) # Slice de string

print(nome[0:12:2]) # Slice de string com passo

print(nome[::-1]) # Slice de string com passo negativo

print(nome.upper()) # Transforma a string em maiúscula

print (nome.split()[0]) # Separa a string em uma lista

print (nome.split()[1]) # Separa a string em uma lista

print(nome.split()) # Separa a string em uma lista

print(nome.replace('Lucas', 'Gabriel')) # Substitui uma string por outra

print(nome.replace('Gabriel', 'Lucas')) # Substitui uma string por outra

print(nome.replace(nome[6:14], 'Gabriel')) # Substitui uma string por outra

print(nome.find('Gabriel')) # Encontra a posição de uma string