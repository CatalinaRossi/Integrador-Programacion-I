lista = []

print("Bienvenido Usuario")
for i in range(0,5):
    lista.append(int(input("Ingrese un número entero, por favor: ")))

print()
print("Su lista de números enteros es: ", lista) 
print()

def sumar(lista):
    total = 0
    for i in range(len(lista)):
        total += lista[i]	
    return total
    
suma = sumar(lista)
print("La suma de los valores es: ", suma)  

def promedio(lista):
    return sumar(lista)/len(lista)

promedio = promedio(lista)
print("El promedio de los valores es: ", promedio)  

def maximo(lista):
    maximo = lista [0]
    for x in lista:
        if x > maximo :
            maximo = x 
    return maximo 

maximo = maximo(lista)
print("El máximo de los valores es:", maximo) 

def minimo(lista):
    return min(lista)

minimo = minimo(lista)
print("El mínimo de los valores es:", minimo) 

print()
print("Muchas gracias por realizar estas operaciones")
print()