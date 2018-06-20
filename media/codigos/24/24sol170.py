vetor = list(range(100))
aux=0
while True:
	vetor[aux]=int(input())
	if vetor[aux] == -1:
		break
	aux=aux+1
aux1=0
while True:
	num=vetor[aux1]
	if vetor[aux1] == -1:
		break
	while num != 1:
		num=num-1
		vetor[aux1]=vetor[aux1]*num
	print(vetor[aux1])
	aux1=aux1+1