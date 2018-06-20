numero1 = float(input())
numero2 = float(input())
numero3 = float(input())

media = (numero1 + numero2 + numero3) / 3

if media >= 7:
    print("aprovado")
elif media < 3:
    print("reprovado")
elif (3 <= media < 7) :
    print("prova final")