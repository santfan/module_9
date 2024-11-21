# Класс исключений
class StepValueError(ValueError):
    pass

# Создадим класс итератора
class Iterator:
    # Функция инициализации
    def __init__(self, start, stop, step=1):
        self.start, self.stop = start, stop
        self.pointer, self.step = start, step
        # Проверка шага (не должен быть 0)
        if self.step == 0:
            # Вызов исключения
            raise StepValueError
    # Функция итератора
    def __iter__(self):
        self.pointer = self.start
        return self
    # Функция подбора следующего элемента
    def __next__(self):
        # Условия выхода из итератора
        if self.step > 0 and self.pointer > self.stop:
            raise StopIteration
        elif self.step < 0 and self.pointer < self.stop:
            raise StopIteration
        # Если условия выхода не наступили
        else:
            temp = self.pointer
            self.pointer += self.step

            # Возврат значения
            return temp

# Пробуем шаг = 0 (должно сработать исключение)
try:
    iter1 = Iterator(100, 200, 0)

    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг не должен быть равен 0')

# Блок создания коллекций
# Шаг по умолчанию 1
iter2 = Iterator(-5, 1)
# Шаг  2
iter3 = Iterator(6, 15, 2)
# Шаг -1
iter4 = Iterator(5, 1, -1)
# Неверные параметры старт меньше стопа а шаг принят по дефолту т.е. 1
# Итератор остановится так как условие self.step > 0 И self.pointer > self.stop
# сразу вызовет raise
iter5 = Iterator(10, 1)

# Вывод результатов
for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()