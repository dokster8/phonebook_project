# Чтение из файла в формате:
# в файле на одной строке хранится все записи, символ разделитель - ,

def read_some_file(some_file):
    f = open(some_file, 'r')
    p = f.readlines()
    l = [i.replace('\n', '').split(',') for i in p]
    f.close()
    return l


# print(read_some_file('read2.csv'))
