"""
Faça um programa que leia a quilometragem de um carro, caso esteja acima
dos 80km/h, multe o carro
"""
km = int(input("Velocidade do carro: "))
if km >= 80:
    print("Você ultapassou o limite, multa de R$150!")
else: 
    print("Velocidade permitida")