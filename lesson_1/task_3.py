"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""

words = ['attribute', 'класс', 'функция', 'type']

result = []
for word in words:
    try:
        bytes(word, 'ASCII')
    except UnicodeEncodeError:
        result.append(word)

print("Невозможно записать в байтовом типе с помощью маркировки b''", result)
