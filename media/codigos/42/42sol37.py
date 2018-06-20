n = int(input())
if n<16:
    print('nao eleitor')
if 18<=n<=65:
    print('eleitor obrigatorio')
if 16<=n<18 or n>65:
    print('eleitor facultativo')
