import numpy as np

n=6
x=[1, 3, 5, 10, 15, 25]
y=[(4.049*0.01), (2.604*0.01), (1.912*0.01), (1.142*0.01), (0.741*0.01), (0.521*0.01)]
yA = []

def calculaYAjustado():
	# print(a1)
	# print(a0)
	for i in range(n):
		# print(x[i])
		# print(a0 / (1+(a1*a0*x[i])))
		yA.append(a0 / (1+(a1*a0*x[i])))

def somatorioQuadrado(vetor):
	soma = 0
	for i in vetor:
		soma += i*i

	# print("Somatório Quadrado = " + str(soma))
	return soma

def somatorio(vetor):
	soma = 0
	for i in vetor:
		soma += i

	# print("Somatório = " + str(soma))
	return soma

def somatorioXY(vetorX, vetorY):
	soma = 0
	for i in range(0, n):
		soma += vetorX[i] * vetorY[i]

	# print("Somatório XY= " + str(soma))
	return soma

def somatorio_y_ya():
	soma = 0
	for i in range(n):
		# print((y[i] - yA[i])*(y[i] - yA[i]))
		soma += (y[i] - yA[i])*(y[i] - yA[i])

	return soma

matrizA = np.array([[somatorioQuadrado(x), somatorio(x)], # som(x)^2 som(x)
					[somatorio(x), n]])					  # som(x)   n
matrizB = np.array([[somatorioXY(x, y)], #som(x*y)
					[somatorio(y)]])	 #som(y)

print("Matriz A")
print(matrizA)
print()
# print()
# print(matrizA.T)
# print()print("Matriz A")
print("Matriz B")
print(matrizB)
print()

print("Matriz A Transposta")
print(matrizA.T)
print()

print("Inversa da multiplicação")
print(np.linalg.inv(np.dot(matrizA.T, matrizA)))
print()
X = np.dot(np.linalg.inv(np.dot(matrizA.T, matrizA)), (np.dot(matrizA.T, matrizB))) #X=inv(A'*A)*(A'*B)

print(X[0])
print(X[1])
# print(X[1])
# print(1/x[1])
a1 = float(X[0])
a0 = 1/x[1]
# print()
# print()

calculaYAjustado()
# print(yA)

# print(X)
R2 = 1 - ( (n * somatorio_y_ya()) / ( n * (somatorioQuadrado(y) - (somatorio(y) * somatorio(y))) ) )
print(n * somatorio_y_ya())
print(n * somatorioQuadrado(y))
print(somatorio(y) * somatorio(y))
print("R2 = " + str(R2))