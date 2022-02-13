# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

def value_and_type(items):
    for i in items:
        b = eval(f'b"{i}"')
        print(f'Слово: {b} | Тип: {type(b)} | Длина: {len(b)}')
        print('')
    print('=' * 50)


str_list = ['class', 'function', 'method']
value_and_type(str_list)
