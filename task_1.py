import random
import timeit
import copy
import sortings

def get_test_data(n):
    """ Генерируем наборы данныз для тестирования """
    return  random.sample(range(n), n)

n = 10000 # Кол-во элементов для тестового набора данных
test_data = get_test_data(n)

# Словарь для сортировки результатов
sort_times = {
    'SORT': timeit.timeit('sortings.simple_sort(copy.deepcopy(test_data))', globals=globals(), number=1),
    'SORTED': timeit.timeit('sorted(copy.deepcopy(test_data))', globals=globals(), number=1),
    'INSERTION': timeit.timeit('sortings.insertion_sort(copy.deepcopy(test_data))', globals=globals(), number=1),
    'MERGE': timeit.timeit('sortings.merge_sort(copy.deepcopy(test_data))', globals=globals(), number=1),
    'BUBBLE': timeit.timeit('sortings.bubble_sort(copy.deepcopy(test_data))', globals=globals(), number=1),
    'SELECTION': timeit.timeit('sortings.selection_sort(copy.deepcopy(test_data))', globals=globals(), number=1),
    'QUICK': timeit.timeit('sortings.quicksort(copy.deepcopy(test_data))', globals=globals(), number=1),
    'SHELL': timeit.timeit('sortings.shell_sort(copy.deepcopy(test_data))', globals=globals(), number=1),
    'RADIX': timeit.timeit('sortings.radix_sort(copy.deepcopy(test_data))', globals=globals(), number=1)
}
sorted_times = sorted(sort_times.items(), key=lambda item: item[1])

for sort_name, time_taken in sorted_times:
    print(f"{time_taken:.6f} сек - {sort_name}")

