#Exemplo Valor Bool
print("Start")

if True:
    print("True")

print("Is")

# Exemplo Usuário:
name = input("Say your name: ")

if name == "Fernando":
    print("Nice to meet you")

elif name == "José":
    print("Hi, José!")

else:
    print("You are not Fernando")

print(f"Hello, {name}")

# Exemplo Pontuação:
score = int(input("Whats score: "))

if score == 10:
    print("You get are A WONDERFULL")
elif score == 9 or score == 8:
    print("Congratulations")
else:
    print("You get an F")

# Exemplo Diferença:
name = input("Whats your name: ")

if not name == "Roddrigo":
    print("Nice to meet you")
else:
    print("Hi!")

#Exemplo Maisc. ou Minus.
name = input("YES OR NO []")