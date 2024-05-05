def ordenacion_topologica(n, restricciones):
    # Crear listas para representar el grafo y los grados de entrada
    sucesores = [[] for _ in range(n)]
    grados_entrada = [0] * n
    
    # Construir el grafo y calcular los grados de entrada
    for tarea_ant, tarea_sig in restricciones:
        sucesores[tarea_ant - 1].append(tarea_sig - 1)
        grados_entrada[tarea_sig - 1] += 1

    # Inicializar la cola con tareas que no tienen predecesores
    cola = [i for i in range(n) if grados_entrada[i] == 0]
    orden_topologico = []

    # Procesar el grafo
    while cola:
        tarea = cola.pop(0)
        orden_topologico.append(tarea + 1)
        
        for sucesor in sucesores[tarea]:
            grados_entrada[sucesor] -= 1
            if grados_entrada[sucesor] == 0:
                cola.append(sucesor)

    # Comprobar si todas las tareas están en el orden topológico
    if len(orden_topologico) != n:
        return None
    return orden_topologico

def solicitar_restricciones(n, num_restricciones):
    restricciones = []
    print("Ingrese las restricciones en formato (i, j) donde i debe preceder a j:")
    for _ in range(num_restricciones):
        i = int(input("Ingrese la tarea que precede (i): "))
        j = int(input("Ingrese la tarea que sigue (j): "))
        if 1 <= i <= n and 1 <= j <= n and i != j:
            restricciones.append((i, j))
        else:
            print("Restricción inválida, intente nuevamente.")
            continue
    return restricciones

def main():
    n = int(input("Ingrese el número de tareas: "))
    num_restricciones = int(input("Ingrese el número de restricciones: "))
    restricciones = solicitar_restricciones(n, num_restricciones)
    print("Restricciones:", restricciones)
    
    orden = ordenacion_topologica(n, restricciones)
    if orden is None:
        print("No se puede ordenar debido a restricciones contradictorias.")
    else:
        print("Orden de tareas:", orden)

if __name__ == "__main__":
    main()
