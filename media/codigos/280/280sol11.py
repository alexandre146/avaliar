
nome = input()
salarioFixo = float(input())
totalDeVendas = float(input())

comissao = totalDeVendas * 0.15
salarioTotal = salarioFixo + comissao
salarioTotal = salarioTotal.__round__(2)
print("TOTAL = R$ %1.2f" %salarioTotal)
