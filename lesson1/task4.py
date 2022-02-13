# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).

def value_and_type(items):
    for i in items:
        b = i.encode('utf-8')
        w = b.decode('utf-8')
        print(f'Кодируем: {b} | Декодируем: {w}')


str_list = ['разработка', 'администрирование', 'protocol', 'standard']
value_and_type(str_list)