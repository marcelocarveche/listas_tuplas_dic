"""
Crie uma função que recebe uma lista e retorna uma nova lista com apenas os elementos únicos

"""

lista = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9]


def unique(lista: list) -> list:
    uniq = []
    for num in lista:
        if lista.count(num) > 1:
            if uniq.count(num) == 0:
                uniq.append(num)

    return uniq


print(unique(lista))
