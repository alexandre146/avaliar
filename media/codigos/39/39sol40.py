n1=float(input())
n2=float(input())
n3=float(input())
media=(n1+n2+n3)/3
if (media >= 7):
	print("aprovado")
if media<3:
	print("reprovado")
if 3<=media<7:
	print("prova final")