#verifique se o número é par

name = input("Whats your name?")
x = int(input("enter a number: ")) #10

# Um numero é par quando o resto da divisão por 2 é igual a 0
if x % 2 == 0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")
