ab=input()
ac=input()
bc=input()
if (ab==ac==bc):
    print('equilatero')
if (ab==ac!=bc or ab==bc!=ac or ac==bc!=ab) :
    print('isosceles')
if(ab!=ac and ac!=bc and ab!=bc) :
    print('escaleno')
  
