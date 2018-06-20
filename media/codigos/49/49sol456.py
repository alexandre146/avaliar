A = float(raw_input())
B = float(raw_input())
C = float(raw_input())

if A==B and B==C:
    print 'equilatero'
if A!=B and B==C or A==C and C!=B or A!=C and B==A:
    print 'isoceles'
if A!=B and B!=C and A!=C: 
    print 'escaleno'