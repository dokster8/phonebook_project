from asyncore import write
from read_format1 import read_some_file as r1
from read_format2 import read_some_file as r2
from write_format1 import write_some_file as w1
from write_format2 import write_some_file as w2
import view


def read_write():
    read_file = view.choose_read_file()
    read_format = view.choose_read_format()
    write_file = view.choose_write_file()
    write_format = view.choose_write_format()
    f = r1(read_file) if read_format == '1' else r2(read_file)
    w1(f, write_file) if write_format == '1' else w2(f, write_file)
