def choose_read_format():           # Выбор формата для чтения
    a = input('Выберите из какого формата считывать. Введите 1 или 2: ')
    print('Выбран первый формат.') if a == '1' else print('Выбран второй формат.') if a == '2' else\
        print('Введено неверное значение. Попробуйте ещё раз.')
    if a != '1' and a != '2':
        return choose_read_format()
    return a


def choose_write_format():          # Выбор формата для записи
    a = input('Выберите в какой формат записывать. Введите 1 или 2: ')
    print('Выбран первый формат.') if a == '1' else print('Выбран второй формат.') if a == '2' else\
        print('Введено неверное значение. Попробуйте ещё раз.')
    if a != '1' and a != '2':
        return choose_write_format()
    return a


def choose_read_file():             # Выбор файла для чтения
    a = input('Выберите из какого файла считывать: ')
    return a


def choose_write_file():             # Выбор файла для записи
    a = input('Выберите в какой файл записывать: ')
    return a

# choose_read_format()
# choose_write_format()
