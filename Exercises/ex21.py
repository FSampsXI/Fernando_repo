from random import randint
numero_aleatorio = randint(1, 5)

name = input("Whats your name?")
chute = int(input("enter a number for 0 to 5:"))
print(f"hello {name} your number is {chute}, and the number is {numero_aleatorio}")
if chute == numero_aleatorio:
    print("you're right")
else:
    print("you missed")
