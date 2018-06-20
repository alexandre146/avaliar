valor1 = float(input())
valor2 = float(input())
valor3 = float(input())

media = (valor1 + valor2 + valor3)/3
if(media < 3):
    print("reprovado")
elif (media >= 7):
    print("aprovado")
else:
    print("prova final")
