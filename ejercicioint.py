lista = []

for i in range(0,5):
    lista.append(int(input("Ingrese un número entero, por favor: ")))

print(lista) #para chequear 

def sumar(lista):
    total = 0
    for i in range(len(lista)):
        total += lista[i]	
    return total
    
suma = sumar(lista)
print("La suma de los numeros es: ", suma) #para chequear 

def funcion_maximo(List_number):
    maximo = lista [0]
    for x in lista:
        if x > maximo :
            maximo = x 
    return maximo 

def promedio(lista):
    return sumar(lista)/len(lista)

promedio = promedio(lista)
print("El Promedio de los valores es: ", promedio) #para chequear 
