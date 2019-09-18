  def valMultiplicacionMatricial(matriz_1,matriz_2):
	if type(matriz_1) and type(matriz_2) == list:
		for i in range(0,len(matriz_1)):
			if type(matriz_1[i]) != list:
				 return print("Error el primer argumento no representa una matriz")
		for i in range(0,len(matriz_2)):
			if type(matriz_2[i]) != list:
				return print("Error el segundo argumento no representa una matriz")
		if len(matriz_1) == len(matriz_2[0]):
			return True
		else:
			return False
	else:
		return print("TypeError: revise los datos de entrada, puede que alguno de ellos no represente una matriz")
def expmatriz(n,m,matriz):
	"""Imprime una lista de lista de forma cuadrada simulando la forma de una matriz"""
	for i in range(0,n):#Recorre todas las lista para convertir 
		for j in range(0,m):
			matriz[i][j] = str(matriz[i][j]) 
	for n in range(0,n):
		var =  print(" ".join(matriz[n]))
	return var
def multiplicacion(matriz_1,matriz_2):
	if valMultiplicacionMatricial(matriz_1,matriz_2) == True:
		matriz_3 = []		
		ij = 0
		for h in range(0,len(matriz_1)):
			lista_3 = []
			while len(lista_3) < len(matriz_1):
				lista_3.append(0)
			matriz_3.append(lista_3)		
			for k in range(0,len(matriz_1[0])):						
				for l in range(0,len(matriz_1)):						
					ij = matriz_1[h][k] * matriz_2[k][l]
					matriz_3[h][l] = matriz_3[h][l] + ij 
		return expmatriz(len(matriz_1),len(matriz_2[0]),matriz_3)
	else:
		return print("No es posible realizar esta multiplicacion")
def productoVectorial(v1,v2):
	i = str(v1[1]*v2[2] - v1[2]*v2[1]) + "i"
	j = str(v1[2]*v2[0] - v1[0]*v2[2]) + "j"
	k = str(v1[0]*v2[1] - v1[1]*v2[0]) + "k"
	return print("{}{}{}".format(i,j,k))
def traspuesta(matriz):
	matriztras = []
	for m in range(0,len(matriz[0])):
		lista = []
		matriztras.append(lista)
		for n in range(0,len(matriz)):		
			lista.append(matriz[n][m])	
	print("la matriz es: ")	
	expmatriz(len(matriz),len(matriz[0]),matriz)
	print("\n La matriz traspuesta es: ")
	expmatriz(len(matriztras),len(matriztras[0]),matriztras)	
	return 

ma = [[1,5,6,8,9],[1,3,2,7,4]]
traspuesta(ma)