# Согласно условию имеем два списка
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Используя списочные выражения выполним задание
# Длина элемента не менее 5
print([len(x) for x in first_strings if len(x) >= 5])

# Из двух списков отберем эелементы одинаковой длинны
second_result = {(x, y) for x in first_strings for y in second_strings if len(x) == len(y)}
print(second_result)

# Из объедененного списка отберем те элементы длинна которых кратна 2
third_result = {x: len(x) for x in (first_strings + second_strings) if not len(x) % 2}
print(third_result)

