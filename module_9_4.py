# Для работы импортируем функцию choice из модуля randon
from random import choice
# Имеем два списка
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Использование lambda-функции
print(list(map(lambda x, y: x == y, first, second)))

# Использование создание функции внутри другой
# Объявим функцию высшего порядка
def get_advanced_writer(file_name):
  # Создадим функцию "на лету"
  def write_everything(*data_set):
    # откроем файл example.txt для чтения
    with open('example.txt', 'w', encoding = 'utf-8') as file:
      # обойдем data_set и запишем данные в файд example.txt
      for elem in data_set:
        file.write(str(elem) + '\n')
  # Вернем результат работы функции
  return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Использование классов для создания вычислений "на лету"
class MysticBall:

  def __init__(self, *words):
    self.words = words

  def __call__(self):
    # Вернем случайно выбранное слово
    return choice(self.words)

# Создадим объект класса MysticBall
first_ball = MysticBall('Да', 'Нет', 'Наверное')
# Выведем результат
print(first_ball())
print(first_ball())
print(first_ball())