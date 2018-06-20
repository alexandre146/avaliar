maior=0

numN=int(input())
numM=int(input())
for x in range(numN,numM+1):
    if(x%numN==0):
        if(x>maior):
            maior=x
if(maior==0):
    print("sem multiplos menores que", numM)
else:
    print(maior)

        
            
    

   
       
