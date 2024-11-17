# Объявим функцию которая принимает список и некоторое количество функций
def apply_all_func(ini_list, *functions):
    # создадим пустой словарь
    result = {}
    # Пробежим по переданным функциям
    for function in functions:
        # Создадим в словаре пары ключ-значение
        result[function.__name__] = function(ini_list)
    # Вернем созданный словарь
    return result

# Проверим результат
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
