# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com
# и преобразовать результаты из байтовового в строковый тип на кириллице.
import subprocess


def ping_yandex(items):
    for url in items:
        ping = ['ping', url]
        subproc_ping = subprocess.Popen(ping, stdout=subprocess.PIPE)

        for line in subproc_ping.stdout:
            print(line.decode('cp866').encode('utf-8').decode('utf-8'))


urls = ['yandex.ru', 'youtube.com']
ping_yandex(urls)
