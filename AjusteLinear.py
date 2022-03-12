import numpy as np

n=6
x = [1, 3, 5, 10, 15, 25]
y = [(4.049)*0.01, (2.604)*0.01, (1.912)*0.01, (1.142)*0.01, (0.741)*0.01, (0.521)*0.01]

def somatorioQuadrado(vetor):
	soma = 0
	for i in vetor:
		soma += i*i

	return soma

def somatorio(vetor):
	soma = 0
	for i in vetor:
		soma += i

	return soma

def somatorioXY(vetorX, vetorY):
	soma = 0
	for i in range(0, n):
		soma += vetorX[i] * vetorY[i]

	return soma

matrizA = np.array([[somatorioQuadrado(x), somatorio(x)], [somatorio(x), n]])
matrizB = np.array([[somatorioXY(x, y)], [somatorio(y)]])

# print(matrizA)
# print()
# print(matrizA.T)
# print()
# print(matrizB)

X = np.dot(np.linalg.inv(np.dot(matrizA.T, matrizA)), (np.dot(matrizA.T, matrizB)))

print(X[0])
print(X[1])

# print(X)