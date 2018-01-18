import xlrd

# 由execl 导出数据
def execl_insert(file_name):
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
def execl_create(file_name):
    


if __name__ == '__main__':
   import sys
   execl_insert(str(sys.argv[1]))

