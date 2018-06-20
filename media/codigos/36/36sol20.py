
num_d = int(input());
num = int(input());
maior_mul = num - (num % num_d)
if maior_mul <= num:
    print(maior_mul);
else:
    print("sem multiplos menores que",num);