a = float(input())
b = float(input())
c = float(input())
media = (a + b + c) / 3
if media >= 7:
	print("aprovado")
if media < 3:
	print("reprovado")
if 3 <= media < 7:
	print("prova final")