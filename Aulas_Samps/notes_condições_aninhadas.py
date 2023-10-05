#Condições Aninhadas(Condições dentro de outras condições)

name = input("Whats your name: ") 

if name == "Fernando":
    print("Nice to meet you")
    age = int(input("How old are u: "))
    if age >= 17:
        print("You are getting older")
    elif age == 16:
        print("You are sixteen")
    else:
        print("You are too young")
else:
    print("You are not Fernando")
    if name == "Pedro":
        print("Hi Pedro!")
