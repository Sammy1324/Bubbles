def merge_sort(arr):
    """
    Ordena una lista de elementos de menor a mayor usando el algoritmo Merge Sort.

    :param arr: Lista de elementos a ordenar
    :return: Lista ordenada
    """
    if len(arr) > 1:
        # Encuentra el punto medio de la lista
        mid = len(arr) // 2

        # Divide la lista en dos mitades
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Llama recursivamente a merge_sort en ambas mitades
        merge_sort(left_half)
        merge_sort(right_half)

        # Fusiona las dos mitades ordenadas
        merge(arr, left_half, right_half)

def merge(arr, left_half, right_half):
    """
    Fusiona dos sublistas ordenadas en una sola lista ordenada.

    :param arr: Lista original que se actualizará con los elementos ordenados
    :param left_half: Sublista izquierda ordenada
    :param right_half: Sublista derecha ordenada
    """
    i = j = k = 0

    # Fusiona los elementos mientras haya elementos en ambas mitades
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Agrega los elementos restantes de la mitad izquierda (si los hay)
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Agrega los elementos restantes de la mitad derecha (si los hay)
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Ejemplo de uso
if __name__ == "__main__":
    lista = [38, 27, 43, 3, 9, 82, 10]
    print("Lista original:", lista)
    merge_sort(lista)
    print("Lista ordenada:", lista)