funcionario=input().split()
comissao=funcionario[2]
parte=comissao*15/100
salario=funcionario[1]+parte
print("TOTAL = R$", str('%.2f'%salario))
