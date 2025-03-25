"""def bubble(listt):
    for i in range(0, len(listt)-1):
        for j in range(0, len(listt)-i-1):
            if (listt[j] > listt[j+1]):
                listt[j], listt[j+1] = listt[j+1], listt[j]
    return listt

nums = [3, 1, 5, 2, 4]
print(bubble(nums))

def improved_bubble(listt):
    i = 0
    control = True
    while (i <= len(listt)-2) and control:
        control = False
        for j in range(0, len(listt)-i-1):
            if (listt[j] > listt[j+1]):
                listt[j], listt[j+1] = listt[j+1], listt[j]
                control = True
        i += 1
        return listt

print(improved_bubble(nums))"""

def bubble_sort(arr):
    """
    Ordena una lista de elementos de menor a mayor usando el algoritmo Bubble Sort.

    :param arr: Lista de elementos a ordenar
    :return: Lista ordenada
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambia los elementos si están en el orden incorrecto
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [5, 3, 8, 4, 2, 7, 1, 6]
    print("Lista original:", lista)
    lista_ordenada = bubble_sort(lista)
    print("Lista ordenada:", lista_ordenada)