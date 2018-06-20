print('Digite trés Números: ')
n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
n3 = float(input('Número 3: '))

if n1<n2 and n1<n3 and n2<n3:
    print('Números em ordem crescente: ')
    print(n1)
    print(n2)
    print(n3)
if n2<n1 and n2<n3 and n1<n3:
    print('Números em ordem crescente: ')
    print(n2)
    print(n1)
    print(n3)
if n3<n1 and n3<n2 and n2<n1:
    print('Números em ordem crescente: ')
    print(n3)
    print(n2)
    print(n1)
if n1<n2 and n1<n3 and n3<n2:
    print('Números em ordem crescente: ')
    print(n1)
    print(n3)
    print(n2)
if n3<n1 and n3<n2 and n1<n2:
    print('Números em ordem crescente: ')
    print(n3)
    print(n1)
    print(n2)
if n2<n1 and n2<n3 and n3<n1:
    print('Números em ordem crescente: ')
    print(n3)
    print(n1)
    print(n2)
print('Tá aí!!!')
