"""def cocktail(listt):
    left = 0
    right = len(listt)-1
    control = True
    while (left < right) and control:
        control = False
        for i in range(left, right):
            if (listt[i] > listt[i+1]):
                control = True
                listt[i], listt[i+1] = listt[i+1], listt[i]
        right -= 1
        for j in range(right, left, -1):
            if (listt[j] < listt[j-1]):
                control = True
                listt[j], listt[j-1] = listt[j-1], listt[j]
        left += 1
        return listt
    
nums = [3, 2, 5, 1, 4]
print(cocktail(nums))"""

def cocktail_sort(arr):
    """
    Ordena una lista de elementos de menor a mayor usando el algoritmo Cocktail Sort.

    :param arr: Lista de elementos a ordenar
    :return: Lista ordenada
    """
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Recorrido hacia adelante
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Si no hubo intercambios, la lista está ordenada
        if not swapped:
            break

        swapped = False
        end -= 1

        # Recorrido hacia atrás
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1

    return arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [5, 3, 8, 4, 2, 7, 1, 6]
    print("Lista original:", lista)
    lista_ordenada = cocktail_sort(lista)
    print("Lista ordenada:", lista_ordenada)