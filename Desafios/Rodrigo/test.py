# Seletor de aluno
# 1) Escreva um programa que permita selecionar um aluno aleatório de um arquivo txt
# 2) Permita que o programa adicione um aluno a lista
# 3) Permita que o programa remova um aluno a lista

"""
import csv
names = []

with open("names.csv") as file:
    reader = csv.DictReader(file)
    print(reader)
    for row in reader:
        names.append(row)


for n in sorted(names, key=lambda n: n["name"]):
    print(f"{n['name']} is from {n['home']}")

--------------------------   

import csv

name = input("whats your name: ")
home = input("Where are you from: ")

with open("names.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
"""