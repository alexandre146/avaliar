
valor_1 = int(input())
valor_2 = int(input())
valor_3 = int(input())

if valor_1 <= valor_2 and valor_1 <= valor_3:
    print(valor_1)
elif valor_2 < valor_1 and valor_2 < valor_3:
    print(valor_2)
elif valor_3 < valor_1 and valor_3 < valor_2:
    print(valor_3)
if valor_1 <= valor_2 and valor_1 >= valor_3:
    print(valor_1)
elif valor_2 <= valor_1 and valor_2 > valor_3:
    print(valor_2)
elif valor_3 <= valor_1 and valor_3 > valor_2:
    print(valor_3)
if valor_1 >= valor_2 and valor_1 <= valor_3:
    print(valor_1)
elif valor_2 > valor_1 and valor_2 < valor_3:
    print(valor_2)
elif valor_3 > valor_1 and valor_3 < valor_2:
    print(valor_3)
