def quicksort(arr):
    """
    Ordena una lista de elementos de menor a mayor usando el algoritmo Quicksort.

    :param arr: Lista de elementos a ordenar
    :return: Lista ordenada
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        menores = [x for x in arr[1:] if x <= pivot]  # Elementos menores o iguales al pivote
        mayores = [x for x in arr[1:] if x > pivot]   # Elementos mayores al pivote
        return quicksort(menores) + [pivot] + quicksort(mayores)

# Ejemplo de uso
if __name__ == "__main__":
    lista = [5, 2, 9, 1, 5, 6]
    print("Lista original:", lista)
    lista_ordenada = quicksort(lista)
    print("Lista ordenada:", lista_ordenada)