i = float(input())
h = float(input())
j = float(input())
media = (i + j + h) / 3
if media >= 7:
	print("aprovado")
if media < 3:
	print("reprovado")
if 3 <= media < 7:
	print("prova final")