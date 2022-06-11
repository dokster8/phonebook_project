# Запись в файл в формате:
# в файле на одной строке хранится одна часть записи, пустая строка - разделитель
from read_format2 import read_some_file as r2
from read_format1 import read_some_file as r1


def write_some_file(some_data, new_file):
    f = open(new_file, 'w')
    l = []
    for i in some_data:
        for j in i:
            l.append(j+'\n')
        l.append('\n')
    for k in range(len(l)-1):
        f.write(l[k])
    f.close()

write_some_file(r1('read1.csv'), 'write1.csv')
