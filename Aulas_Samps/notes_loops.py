"""""
for i in [1,2,3]:
    print(i)
"""
#só posso usar o "for" com um objeto inteirado
#range é uma função q lida com inteiros
#função enumerate estudar sobre

for i in range(5,10):
    print(i)

alunos = ["Rodrigo", "Antonio", "Pedro"]

for aluno in range(len(alunos)):
    print(aluno+1, alunos[aluno])
