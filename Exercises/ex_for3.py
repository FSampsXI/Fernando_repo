# Desenvolva um programa que calcule a soma de todos os números
# multiplos de três entre 1 e 500
# E mostre quais são 

lista = []
soma = 0

for i in range(1, 501):
    if(i % 3 == 0):
        lista.append(i)
print(lista)

for x in range(len(lista)):
    soma = soma + lista[x]

print(soma)
    
#estudar esse código, by: Biel