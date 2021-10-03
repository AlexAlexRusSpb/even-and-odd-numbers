# Напишите функцию, определяющую, сколько в сгенерированном списке четных и нечетных чисел.
# Задания со звездочкой:
# 1 Напишите аннотацию типов ()
# 2 Протестируйте функцию с помощью doctest или assert

import random
from doctest import testmod
# есть генератор, который работает так
begin: int = random.randint(-100500, 100500)
generated: int = [i for i in range(begin, begin + random.randint(0, 100500))]

def find_even_and_odd_numbers(generated):
    """
    Inconing random array int numbers, return count odd and even
    >>> find_even_and_odd_numbers([2,3])
    [1, 1]
    >>> find_even_and_odd_numbers([2,3,-1,4,5])
    [3, 2]
    >>> find_even_and_odd_numbers([])
    [0, 0]
    >>> find_even_and_odd_numbers([1])
    [1, 0]
    """
    #assert len(generated) != 0, 'Список generated пуст'
    odd_number_cnt : int = len(list(filter(lambda x: x%2 != 0,generated)))
    even_number_cnt: int = len(generated) - odd_number_cnt
    return [odd_number_cnt,even_number_cnt]
    
if __name__ == "__main__":
    testmod(verbose = True)