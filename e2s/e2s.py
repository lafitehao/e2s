#!/usr/bin/python3

import lib.execlparser
import lib.sqlbuilder
import xlrd

parser = lib.execlparser
builder = lib.sqlbuilder

def build_insert_from_execl(file_name):
    print(
        builder.build_insert(
            parser.parse_data(
                xlrd.open_workbook(file_name).sheets[0])))

def build_create_from_execl(file_name):
    print(
        builder.build_table(
            parser.parse_table(
                xlrd.open_workbook(file_name).sheets[0])))

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        order_code = sys.argv[1]

        if order_code == '-c':
            build_insert_from_execl(sys.argv[2])
        elif order_code == '-i':
            build_create_from_execl(sys.argv[2])
    else:
        print('command_args ::== (-c/-r file_name)')
