quantDivisores = 0

for i in range(5):
    num = int(input())
    if(num % 3 == 0):
        quantDivisores += 1

if(quantDivisores != 0):
    print(quantDivisores)

else:
    print("O numero nao possui divisores multiplos de 3!")
