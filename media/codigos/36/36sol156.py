num1 = int(input())
num2 = int(input())

resultado = num2 / num1
resultado2 = num1 * int(resultado)

if(resultado2 == 0):
     print("sem multiplos menores que", num2)

else:
    print(resultado2)
