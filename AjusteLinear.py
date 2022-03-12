import numpy as np
import matplotlib.pyplot as plt
import math

n=6
x=[1, 3, 5, 10, 15, 25]
y=[(4.049*0.01), (2.604*0.01), (1.912*0.01), (1.142*0.01), (0.741*0.01), (0.521*0.01)]
yA = []

def plot():
	plt.plot(x, y, color="green")
	plt.plot(x, yA, color="red")
	plt.xlim(1, 25)
	plt.xticks(np.linspace(1, 25, 20, endpoint=True))
	plt.ylim(24.7, 191.9)
	plt.yticks(np.linspace(24.7, 191.9, 20, endpoint=True))
	plt.show()

def calculaYAjustado():
	# print(a1)
	# print(a0)
	for i in range(n):
		# print(x[i])
		# print(a0 / (1+(a1*a0*x[i])))
		yA.append(a0 / (1+a1*a0*x[i]))

def somatorioQuadrado(vetor):
	soma = 0
	for i in vetor:
		soma += i*i

	# print("Somatório Quadrado de Y = " + str(soma))
	return soma

def somatorio(vetor):
	soma = 0
	for i in vetor:
		soma += i

	# print("Somatório = " + str(soma))
	return soma

def somatorioB(vetor):
	soma = 0
	for i in vetor:
		soma += 1/i

	# print("Somatório = " + str(soma))
	return soma

def somatorioXY(vetorX, vetorY):
	soma = 0
	for i in range(0, n):
		soma += vetorX[i] * vetorY[i]

	# print("Somatório XY= " + str(soma))
	return soma

def somatorioXYB(vetorX, vetorY):
	soma = 0
	for i in range(0, n):
		soma += vetorX[i] * 1/vetorY[i]

	# print("Somatório XY= " + str(soma))
	return soma

def somatorio_y_ya():
	soma = 0
	for i in range(n):
		# print(y[i])
		# print(yA[i])
		# print((y[i] - yA[i])*(y[i] - yA[i]))
		soma += (y[i] - yA[i])*(y[i] - yA[i])

	# print("Somatório de y - ya = " + str(soma))
	return soma

matrizA = np.array([[somatorioQuadrado(x), somatorio(x)], # som(x)^2 som(x)
					[somatorio(x), n]])					  # som(x)   n
matrizB = np.array([[somatorioXYB(x, y)], #som(x*y)
					[somatorioB(y)]])	 #som(y)

multATeA = np.dot(matrizA.T, matrizA)
# print("Matriz AT * Matriz A")
# print(multATeA)
# print()
multATeB = np.dot(matrizA.T, matrizB)
# print("Matriz AT * Matriz B")
# print(multATeB)
# print()
invMultATeA = np.linalg.inv(multATeA)
# print("Inversa de AT * A")
# print(invMultATeA)
# print()
X = np.dot(invMultATeA, multATeB) #X=inv(A'*A)*(A'*B)
# print("X = ")
# print(X)
# print()
# print()

# print(X[0])
# print(1/X[1])
# print(X[1])
# print(1/x[1])
a1 = float(X[0])
a0 = float(1/X[1])
# print("a1 = " + str("{:.4}".format(a1)))
print()
print()
print()
print("a1 = " + str(round(a1, 4)))
# print("a0 = " + str("{:.4}".format(a0)))
print("a0 = " + str(round(a0, 4)))

calculaYAjustado()
# print("Vetor do Y Ajustado")
# print(yA)
# print()
# print(yA)

somatorioY_YA = somatorio_y_ya()
somatorioY2 = somatorioQuadrado(y)
somatorio2Y = somatorio(y) * somatorio(y) # 1 - (3,6109604351 / 0,005343)
# print("S1 = " + str(somatorioY_YA))
# print("S2 = " + str(somatorioY2))
# print("S3 = " + str(somatorio2Y))
R2 = 1 - ( (n * somatorioY_YA) / ( (n * somatorioY2 - somatorio2Y) ) )
# R2 = R2 / 100
# print(n * somatorio_y_ya())
# print(n * somatorioQuadrado(y))
# print(somatorio(y) * somatorio(y))
# print("R2 = " + str("{:.4}".format(R2)))
print("R2 = " + str(round(R2, 4)))
# print()
# print()
# print()

# for i in range(n):
# 	print(yA[i])

# for i in range(n):
# 	print(y[i])
# plot()