n1 = float(input("Digite o 1º valor: "))
n2 = float(input("Digite o 2º valor: "))
n3 = float(input("Digite o 3º valor: "))
m = n1 + n2 + n3 / 3
if m >= 7:
    print ("aprovado")
elif m < 3:
    print ("reprovado")
elif 3 <= m < 7:
    print ("prova final")

