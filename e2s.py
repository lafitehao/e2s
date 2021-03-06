#!/usr/bin/python3

from e2slib import execlparser, sqlbuilder
import xlrd
import sys
sys.path.append('./lib')

parser = execlparser
builder = sqlbuilder

def build_insert_from_execl(file_name, sheet_index):
    book = xlrd.open_workbook(file_name)
    sh = book.sheet_by_index(int(sheet_index))
    print(
        builder.build_insert(
            parser.parse_data(sh)))

def build_create_from_execl(file_name):
    sh = xlrd.open_workbook(file_name).sheet_by_index(0)
    print(
        builder.build_table(
            parser.parse_table(sh)))

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        order_code = sys.argv[1]

        if order_code == '-c':
            build_create_from_execl(sys.argv[2])
        elif order_code == '-i':
            sheet_index = 0
            try:
                sheet_index = sys.argv[3]
            except:
                pass
            build_insert_from_execl(sys.argv[2], sheet_index)
    else:
        print('command_args ::== (-c/-r file_name)')
