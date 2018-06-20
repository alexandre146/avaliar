nomeVendedor = input()
salariofixo = float(input())
vendasEfetuadas = float(input())

salarioBonus = vendasEfetuadas * 0.15
salarioTotal = salariofixo + salarioBonus
print("TOTAL = R$ %.2f"%salarioTotal)
