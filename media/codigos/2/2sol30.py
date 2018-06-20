
res = None

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 < n2:
    res = n1;
    n1 = n2;
    n2 = res;

if n1 < n3:
    res = n1;
    n1 = n3;
    n3 = res;

if n2 < n3:
    res = n2;
    n2 = n3;
    n3 = res;

print (n3);
print (n2);
print (n1)