quantDivisores3 = 0

num = int(input())

for divisores in range (1, num + 1):

    if(num % divisores == 0):
        if(divisores % 3 == 0):
            quantDivisores3 = quantDivisores3 + 1

if(quantDivisores3 > 0):
    print(quantDivisores3)
else:
    print("O numero nao possui divisores multiplos de 3!")
