# Чтение из файла в формате:
# в файле на одной строке хранится одна часть записи, пустая строка - разделитель

def read_some_file(some_file):
    l = []
    st = ''
    f = open(some_file, 'r')
    p = f.readlines()
    for j in p:
        st += j.replace('\n', '') + ','
        if j == '\n':
            l.append(st[:-2].split(','))
            st = ''
    l.append(st[:-1].split(','))
    f.close()
    return l


# print(read_some_file('read1.csv'))
