eleitor=int(input())
x=16
a=18
f=65
if eleitor<x:
   print("nao eleitor")
   
if eleitor>=a:
   print("eleitor obrigatorio")

if eleitor>=f:
    print("eleitor facultativo")

if eleitor<a and eleitor>=x:
    print("eleitor facultativo")
