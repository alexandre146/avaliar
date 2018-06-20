
menor = 0
medio = 0
maior = 0

n1,n2,n3 = int(input()),int(input()),int(input())

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else: menor = n3

if n1 > n2 and n1 > n3:
    maior = n1    
elif n2 > n1 and n2 > n3:
    maior = n2
else: maior = n3    

if n1 > menor and n1 < maior:
    medio = n1
elif n2 > menor and n2 < maior:
    medio = n2
else: medio = n3      
 
print(menor)
print(medio)
print(maior)


