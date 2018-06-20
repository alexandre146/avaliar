nome = str(input())
s_fixo = float(input())
vendas = float(input())
v_15 = vendas * 0.15
total = s_fixo + v_15
total2 = round(total,2)
print ("TOTAL = R$ " + str(total2))
