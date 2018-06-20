a=input()
b=input()

b=b[::]
p=b.index(" ")
salario=b[:p]
vendas=b[p:]

salario=float(salario)
vendas=float(vendas)

m=vendas*0.15

salario2=salario+m

print("%.2f"%(salario2))
