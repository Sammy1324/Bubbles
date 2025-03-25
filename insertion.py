def insertion_sort(arr):
    """
    Ordena una lista de elementos de menor a mayor usando el algoritmo de inserción.

    :param arr: Lista de elementos a ordenar
    :return: Lista ordenada
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Mueve los elementos mayores que la clave una posición adelante
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [5, 2, 9, 1, 5, 6]
    print("Lista original:", lista)
    lista_ordenada = insertion_sort(lista)
    print("Lista ordenada:", lista_ordenada)