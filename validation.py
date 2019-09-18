"""Este modulo tiene las siguientes funciones de validacion de variables:
1-. valInt
2-. valFloat
3-. valComplex
4-. ValList """


def valInt(*args):
	"""Validacion de datos de tipo entero.
	ValInt(Int,tuple/list)
	El primero argumento debe ser un entero y debe estar en intervalo abierto en caso de ser tuple o en el intervalo
	cerrado en caso de ser list, para que la funcion arroje True
	 """
	if type(args[0]) != int: #Si el primer argumentos no es un entero directamente la funcion debe arrojar false
		val = print(False)		
	else:						 #Si se ejecuta esta parte de la funcion es porque el primer argumento es un entero
		if len(args) == 1 :
			val = print(True)
		else:
			if type(args[1]) == list or type(args[1]) == tuple:
				if args[1][0] > args[1][1] or len(args[1]) > 2:
					val = print("ValueError")
				elif type(args[1]) == tuple:
					val = print(args[0] < args[1][1] and args[0] > args[1][0])
				else:
					val = print(args[0] <= args[1][1] and args[0] >= args[1][0])
			else:
				val = print("TypeError")
	return val				

def valFloat(*args):
	if type(args[0]) != float: #Si el primer argumentos no es un entero directamente la funcion debe arrojar false
		val = print(False)		
	else:						 #Si se ejecuta esta parte de la funcion es porque el primer argumento es un entero
		if len(args) == 1 :
			val = print(True)
		else:
			if type(args[1]) == list or type(args[1]) == tuple:
				if args[1][0] > args[1][1] or len(args[1]) > 2:
					val = print("ValueError")
				elif type(args[1]) == tuple:
					val = print(args[0] < args[1][1] and args[0] > args[1][0])
				else:
					val = print(args[0] <= args[1][1] and args[0] >= args[1][0])
			else:
				val = print("TypeError")
	return val

def valComplex(*args):
	if type(args[0]) != complex: #Si el primer argumentos no es un entero directamente la funcion debe arrojar false
		val = print(False)		
	else:						 #Si se ejecuta esta parte de la funcion es porque el primer argumento es un entero
		if len(args) == 1 :
			val = print(True)
		else:
			if type(args[1]) == list or type(args[1]) == tuple:
				if args[1][0] > args[1][1] or len(args[1]) > 2:
					val = print("ValueError")
				elif type(args[1]) == tuple:
					val = print(args[0] < args[1][1] and args[0] > args[1][0])
				else:
					val = print(args[0] <= args[1][1] and args[0] >= args[1][0])
			else:
				val = print("TypeError")
	return val

def valList(*args):
	if len(args) == 3:
		if args[2] != "value" and args[2] != "len":
			val = print("ValueError")
		elif type(args[2]) == str and type(args[1]) == int or type(args[1]) == list:
			if args[2] == "value":
				val = print(type(args[0]) == list and type(args[1]) == list and args[0] == args[1])
			elif args[2] == "len" :
				val = print(type(args[0]) == list and type(args[1]) == int and len(args[0]) == args[1])
		else:
			val = print("TypeError")		
	elif len(args) == 1:
		val = print(type(args[0]) == list)
	return val

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


	

