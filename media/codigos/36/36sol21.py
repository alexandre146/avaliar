
num_d = int(input());
num = int(input());
maior_mul = num - (num % num_d)
while num_d > 0:
    if maior_mul <= num:
        print(maior_mul);
    else:
        print("sem multiplos menores que",num);
    num_d = int(input());
    num = int(input());