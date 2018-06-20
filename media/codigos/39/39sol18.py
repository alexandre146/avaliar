x = float(input())
y = float(input())
z = float(input())
media = float((x+y+z)/3)
if(media >= 7):
    print("aprovado")
if(media < 3):
    print("repovado")
if(media >= 3 and media < 7):
    print("prova final")
