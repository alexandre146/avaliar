nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
resultado = (nota1+nota2+nota3)/3

if(resultado>=7):
    print("aprovado")

if(resultado<7 and resultado>3):
    print("prova final")

if(resultado<=3):
    print("reprovado")
