"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
import chardet

words = ['разработка', 'администрирование', 'protocol', 'standard']

for word in words:
    word = word.encode('UTF-16')
    print(word)
    res = chardet.detect(word)
    print(word.decode(res['encoding']))
