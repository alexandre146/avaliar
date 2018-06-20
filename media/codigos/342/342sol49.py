contDivisor = 0
num = int(input())

for i in range(num,0,-1):

    if(i % 3== 0):

        contDivisor += 1
        
if(contDivisor > 0):
    print(contDivisor)
else:
    print("O numero não possui divisores multiplos de 3")
