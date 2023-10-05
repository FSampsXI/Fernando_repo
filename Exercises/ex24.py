"""
Faça um programa que leia a distância em km de uma viagem, se a distância
for menor ou igual a 200km cobre 50 centavos por km rodado, caso contrário
cobre 45 centavos.
"""
distancia = int(input("Quantos km? "))
if distancia >= 200:
    valor_cobrado = 0.50 * distancia
    print(f"O valor será multiplicado por 0.50. O valor a ser pago é: {valor_cobrado}")
else:
    valor_cobrado_menor = 0.45 * distancia
    print (f"O valor será multiplicado por 0.45. O valor a ser pago é: {valor_cobrado_menor}")