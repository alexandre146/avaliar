nota1 = float( input() )
nota2 = float( input() )
nota3 = float( input() )
mediatotal = (nota1+nota2+nota3)/3

if mediatotal >= 7:
    print("aprovado")
if mediatotal < 3:
    print("reprovado")
if mediatotal < 7:
    print("prova final")
