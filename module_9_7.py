# Функция декоратор
def is_praim(func):
    def control(*args):
        # Возьмем декорируемую функцию
        sum_func = func(*args)
        for i in range(2, sum_func):
            if sum_func % i == 0:
                print('Сумма число Составное')
                return sum_func
            print('Сумма число Простое')
            return sum_func
    return control

# Декорируемая функция
def sum_three(*args):
    return sum(args)
# Проверка работы декорируемой функции
print(sum_three(21, 3, 6))

# Обернем в декоратор функцию sum_three()
@is_praim
def sum_three(*args):
    return sum(args)
# Проверка на тесте домашнего задания
result = sum_three(2, 3, 6)
print(result)