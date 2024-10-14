from math import inf # импорт бесконечности
def divide(first, second): # создание функции которая принимает 2 параметра фёрст и секонд
    if second == 0:
        return inf
    return first / second