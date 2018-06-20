contNum = 1
produto = 1
num = int(input())
while (num != -1):
    if (num >= 0) and (num <= 12):
        while (contNum <= num):
            produto *= contNum
            contNum += 1
        print (produto)
    produto = 1
    contNum = 1
    num = int(input())
    
            
