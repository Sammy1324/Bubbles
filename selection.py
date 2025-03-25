"""def selection(listt):
    for i in range(0, len(listt)-1):
        minimum = i
        for j in range(i+1, len(listt)):
            if (listt[j] < listt[minimum]):
                minimum = j
        listt[i], listt[minimum] = listt[minimum], listt[i]
    return listt

nums = [2, 4, 3, 5, 1]
print(selection(nums))"""

def selection_sort(arr):
    """
    Ordena una lista de elementos de menor a mayor usando el algoritmo Selection Sort.

    :param arr: Lista de elementos a ordenar
    :return: Lista ordenada
    """
    n = len(arr)
    for i in range(n):
        # Encuentra el índice del elemento mínimo en la sublista restante
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Intercambia el elemento mínimo con el primer elemento de la sublista
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [2, 4, 3, 5, 1]
    print("Lista original:", lista)
    lista_ordenada = selection_sort(lista)
    print("Lista ordenada:", lista_ordenada)