"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet


def ping_resource(url):
    ARGS = ['ping', url]
    YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)

    for line in YA_PING.stdout:
        result = chardet.detect(line)
        print(line.decode(result['encoding']))


ping_resource('yandex.ru')
ping_resource('youtube.com')
