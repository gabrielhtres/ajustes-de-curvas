X = [1.5, 2.0, 2.5, 3.0]
Y = [2.1, 3.2, 4.4, 5.8]

def somatorioQuadrado(vetor):
	soma = 0
	for x in vetor:
		soma+=(x*x)

	return soma

def somatorio(vetor):
	soma = 0
	for x in vetor:
		soma+=x

	return soma

def somatorioXY(vetorX, vetorY):
	soma = 0
	for x in range(0, len(vetorX)):
		soma+=vetorX[x]*vetorY[x]

	return soma

print("Somatorio Quadrado de X = " + str(somatorioQuadrado(X)))
print("Somatorio de X = " + str(somatorio(X)))
print("Somatorio de X * Y = " + str(somatorioXY(X, Y)))
print("Somatorio de Y = " + str(somatorio(Y)))