""" Для удобства вынес сюда функции сортировки """

def simple_sort(data):
    return data.sort()

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(0, n-i-1): 
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j] 
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def shell_sort(array):
    n = len(array)  # Довжина масиву
    interval = n // 2  # Початковий інтервал

    # Продовжуємо сортувати поки інтервал більше 0
    while interval > 0:
        for i in range(interval, n):  # Проходимо по елементах масиву
            temp = array[i]  # Зберігаємо поточний елемент
            j = i
            # Переміщуємо елементи, що більше temp, на інтервал назад
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp  # Вставляємо temp на правильне місце
        interval //= 2  # Зменшуємо інтервал вдвічі
    return array  # Повертаємо відсортований масив

def radix_sort(nums):
    RADIX = 10  # Базова система числення (десяткова система)
    placement = 1  # Початковий розряд
    max_digit = max(nums)  # Максимальне число у масиві для визначення кількості розрядів

    # Продовжуємо сортувати, поки розряд менший за максимальне число
    while placement <= max_digit:
        # Створюємо "кошики" для кожного розряду
        buckets = [[] for _ in range(RADIX)]
        # Розподіляємо числа по кошикам відповідно до поточного розряду
        for i in nums:
            temp = (i // placement) % RADIX
            buckets[temp].append(i)
        # Оновлюємо масив, об'єднуючи числа з кошиків
        a = 0
        for b in range(RADIX):
            for i in buckets[b]:
                nums[a] = i
                a += 1
        # Переходимо до наступного розряду
        placement *= RADIX
    return nums