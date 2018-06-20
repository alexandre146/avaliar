nome = str(input())
s_fixo = float(input())
vendas = float(input())
v_15 = vendas * 0.15
bonus = s_fixo + v_15
total = (s_fixo + bonus)
print (total + math.ceil(total))
