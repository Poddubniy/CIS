# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.

def not_bytes(items):
    for i in items:
        try:
            bytes(i, 'ascii')
        except UnicodeEncodeError:
            print(f'Слово "{i}" невозможно записать в байтовом типе')


str_list = ['attribute', 'класс', 'функция', 'type']
not_bytes(str_list)
