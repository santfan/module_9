# Имеем два списка
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Используя генераторную сборку zip(), создадим генераторную сборку,
# которая высчитывает разницу длин элементов, если эти длины не равны
first_result  = [(len(i[0]) - len(i[1])) for i in zip(first, second) if len(i[0]) != len(i[1])]
print (list(first_result))

# Создадим генераторную сборку, которая попарно сравнивает длины элеметов списков first и second
second_result = [len(first[i]) == len(second[i]) for i in range(len(first))]
print(list(second_result))