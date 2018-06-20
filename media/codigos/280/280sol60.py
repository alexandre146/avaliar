nome=str(input())
salario_fixo=float(input())
total_vendas=float(input())
bonus=(15/100 * total_vendas)
salario= salario_fixo+bonus
print('%.2f' % salario)
