# Стандартными методами задача решается так
text = 'abc'
for i in range(len(text)):
    for j in range(len(text) - i):
        print(text[j:j + i + 1])
print('Первый вариант')
# Обернем данный код в функцию и вызовем ее
def all_variants_1(text):
    result = []
    for i in range(len(text)):
        for j in range(len(text) - i):
            result.append(text[j:j + i + 1])
    return result

a = all_variants_1('abc')
# В силу того что возвращается список распакуем его при выводе
print(*a, sep='\n')
print('Второй вариант')
# Обратим данную функцию в функцию-генератор
def all_variants_2(text):

    for i in range(len(text)):
        for j in range(len(text) - i):
            yield text[j:j + i + 1]

# Вызовем данную функцию
a = all_variants_2("abc")
for i in a:
    print(i)
print('Третий вариант')
# И наконец используя списковые сборки преобразуем нашу функцию-генератор
def all_variants_3(text):
    yield (text[j:j + i + 1] for i in range(len(text)) for j in range(len(text) - i))

# Вызовем функцию
a = all_variants_3("abc")
for i in a:
    # Следует учесть что списковая сборка возвращает список поэтому используем распаковку
    print(*i, sep='\n')
print('Четвертый вариант')