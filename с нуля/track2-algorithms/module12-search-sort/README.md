# Модуль 12. Поиск и сортировки

Линейный и бинарный поиск, «ручные» сортировки (пузырьковая, вставками,
выбором, слиянием, быстрая), рекурсия, сортировка по ключу и здоровый
смысл: когда писать своё, а когда брать встроенный `sorted`.

Формат задач — функции. В задачах 4–9 встроенные `sort`/`sorted` запрещены —
цель в самом алгоритме.

---

## Шпаргалка

### Линейный поиск

```python
for i, item in enumerate(items):
    if item == x:
        return i
return -1
```

### Бинарный поиск (только в отсортированном списке!)

```python
lo, hi = 0, len(items) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if items[mid] == x:
        return mid
    if items[mid] < x:
        lo = mid + 1
    else:
        hi = mid - 1
return -1
```

Каждый шаг вдвое сужает диапазон: для миллиона элементов хватает ~20 шагов.

### Пузырьковая сортировка

```python
result = items[:]
for i in range(len(result) - 1):
    for j in range(len(result) - 1 - i):
        if result[j] > result[j + 1]:
            result[j], result[j + 1] = result[j + 1], result[j]
```

Соседние элементы меняются местами, пока «тяжёлые» не всплывут в конец.

### Сортировка вставками

```python
result = items[:]
for i in range(1, len(result)):
    current = result[i]
    j = i - 1
    while j >= 0 and result[j] > current:
        result[j + 1] = result[j]
        j -= 1
    result[j + 1] = current
```

Каждый новый элемент «заталкивается» на место в уже отсортированной части —
как карты в руке.

### Сортировка выбором

На каждом шаге ищите минимум в остатке и меняйте местами с первым
элементом остатка.

### Рекурсия

```python
def factorial(n):
    if n <= 1:          # базовый случай — без него бесконечный спуск
        return 1
    return n * factorial(n - 1)
```

Сортировка слиянием: разделить список пополам, отсортировать каждую часть
рекурсивно, слить два упорядоченных списка. Быстрая (quick sort): выбрать
опорный элемент, разложить на «меньшие / равные / большие», рекурсивно
отсортировать крайние и склеить.

### Слияние двух упорядоченных списков

```python
i = j = 0
merged = []
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        merged.append(a[i]); i += 1
    else:
        merged.append(b[j]); j += 1
merged.extend(a[i:]); merged.extend(b[j:])
```

### Встроенная сортировка и ключ

```python
sorted(items)                       # числа/строки — по возрастанию
sorted(items, key=abs)              # по модулю
sorted(words, key=lambda w: (len(w), w))   # по длине, потом по алфавиту
```

Правило: `sorted` — правильный выбор в реальном коде; «ручные» сортировки
пишут, чтобы понять, как они работают и почём O(n²) против O(n log n).

---

## Задачи

| # | Файл | Функция | Сложность |
|---|------|---------|-----------|
| 1 | `t12_01_linear_search.py` | `linear_search(items, x)` | разминка |
| 2 | `t12_02_binary_search.py` | `binary_search(items, x)` | база |
| 3 | `t12_03_count_in_range.py` | `count_in_range(items, lo, hi)` | база |
| 4 | `t12_04_bubble_sort.py` | `bubble_sort(items)` | база |
| 5 | `t12_05_insertion_sort.py` | `insertion_sort(items)` | база |
| 6 | `t12_06_selection_sort.py` | `selection_sort(items)` | база |
| 7 | `t12_07_merge_sorted.py` | `merge_sorted(a, b)` | база+ |
| 8 | `t12_08_merge_sort.py` | `merge_sort(items)` | ★ |
| 9 | `t12_09_quick_sort.py` | `quick_sort(items)` | ★ |
| 10 | `t12_10_is_sorted.py` | `is_sorted(items)` | база |
| 11 | `t12_11_sorted_by_abs.py` | `sorted_by_abs(items)` | база |
| 12 | `t12_12_swap_count.py` | `swap_count(items)` | база+ |
| 13 | `t12_13_dedupe_sorted.py` | `dedupe_sorted(items)` | база+ |
| 14 | `t12_14_kth_smallest.py` | `kth_smallest(items, k)` | база+ |
| 15 | `t12_15_insert_position.py` | `insert_position(items, x)` | база+ |
| 16 | `t12_16_sort_words_by_length.py` | `sort_words_by_length(words)` | ★ |
| 17 | `t12_17_sort_dict_by_value.py` | `sort_dict_by_value(d)` | ★ |
