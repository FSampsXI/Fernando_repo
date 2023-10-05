# Seletor de aluno
# 1) Escreva um programa que permita selecionar um aluno aleatório de um arquivo txt
# 2) Permita que o programa adicione um aluno a lista
# 3) Permita que o programa remova um aluno a lista

import csv

def escrever_lista(name, home):
        with open("names.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "home"])
            writer.writerow({"name": name, "home": home})

choice = input("Digite a para adcionar alunos ou r para remover: ")
if choice == "a":
    name = input("whats your name: ")
    home = input("Where are you from: ")
    escrever_lista(name, home)

# para remover: Pegar o conteúdo do arquivo e dar um jeito de abri-lo no python  em forma de lista de dicionários
# quando der um jeito de inteirar por eles, e assim selecionar oque será removido da lista
# e sobreescrever no arquivo csv

names = []

with open("names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        names.append(row)


for n in sorted(names, key=lambda n: n["name"]):
    print(f"{n['name']} is from {n['home']}")
