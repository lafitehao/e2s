#!/usr/bin/python3

import xlrd

# 由execl 导出数据
def execl_to_insert(file_name):
    table_name = file_name.split('.')[0]
    data = xlrd.open_workbook(file_name)
    table = data.sheet_by_index(0)

    # 抽取表字段
    fields = table.row_values(0)
    fields_str = ''
    for field in fields:
        if field != '':
            fields_str += (field + ',')

    fields_str = 'insert into ' + table_name + '(' + fields_str[0:-1] + ') values ('

    for i in range(1,table.nrows):
        values_str = ''
        for j in range(1, table.ncols):
            values_str += '\''  + str(table.cell(i, j).value) + '\','
            print(fields_str + values_str[0:-1] + ');')

# 由execl 导出建表语句
def parse_execl_to_table(sh):
    tables = []

    if sh.cell_value(1, 0) != 0:
        print('表格数据格式不正确，请重新确认。')
    else:
        import e2slib
        for i in range(1, sh.nrows):
            row_num = sh.cell_value(i, 0)

            if row_num == 0:
                tables.append(e2slib.MyTable(sh.cell_value(i, 1), sh.cell_value(i, 2)))
            elif row_num != '':
                table = tables[len(tables) - 1]
                if sh.cell_value(i, 2) != '':
                    if sh.cell_value(i, 5) != '':
                        table.set_pk(sh.cell_value(i, 2))
                    table.add_col(sh.cell_value(i, 1), sh.cell_value(i, 2),
                                  sh.cell_value(i, 3), sh.cell_value(i, 4))

    return tables

def print_sql_of_create_table(tables):
    for i in range(len(tables)):
        print(tables[i].build_table())

def execl_to_create(file_name):
    print_sql_of_create_table(
        parse_execl_to_table(
            xlrd.open_workbook(file_name).sheet_by_index(0)))

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        order_name = sys.argv[1]
        file_name = sys.argv[2]
        if order_name == '-c':
            execl_to_create(file_name)
        elif order_name == '-i':
            execl_to_insert(file_name)
    else:
        print('command_args ::= (-c/-i file_name)')


