#Ejercicio 4: Ordenación por inserción dicotómica


def ordenacion_por_insercion_dicotomica_con_auxiliar(t):
    def busqueda_binaria(arr, valor, inicio, fin):
        if inicio == fin:
            if arr[inicio] > valor:
                return inicio
            else:
                return inicio + 1
        if inicio > fin:
            return inicio

        medio = (inicio + fin) // 2
        if arr[medio] < valor:
            return busqueda_binaria(arr, valor, medio + 1, fin)
        elif arr[medio] > valor:
            return busqueda_binaria(arr, valor, inicio, medio - 1)
        else:
            return medio

    r = []
    for valor in t:
        posicion = busqueda_binaria(r, valor, 0, len(r) - 1)
        r.insert(posicion, valor)
    return r

def obtener_numeros_del_usuario():
    while True:
        entrada = input("Introduce una lista de números separados por comas (ej. 5,3,8,1): ")
        try:
            # Intentar convertir la entrada en una lista de enteros
            numeros = [int(x.strip()) for x in entrada.split(',')]
            return numeros
        except ValueError:
            # Manejar el caso en que la entrada no pueda ser convertida a entero
            print("Error: Asegúrate de que todos los elementos sean números enteros y estén correctamente separados por comas.")

# Solicitar números al usuario
numeros_usuario = obtener_numeros_del_usuario()

# Ordenar los números usando la función de ordenación por inserción dicotómica
numeros_ordenados = ordenacion_por_insercion_dicotomica_con_auxiliar(numeros_usuario)

# Imprimir la lista ordenada
print("Lista ordenada:", numeros_ordenados)
 
