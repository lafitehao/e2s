from . import blueprint
sql_table = 'drop table {table_code} cascade constraints;\n' +\
               'create table {table_code}\n' +\
               '(\n' +\
               '{fields}\n' +\
               'constraint PK_{table_code} primary key ({pk_code})\n' +\
               ');\n' +\
               'comment on table {table_code} is {table_name};\n' +\
               '{field_comms}\n'
sql_field = '{code} {c_type} {not_null},\n'
sql_field_comm = 'comment on fieldumn {table_code}.{field_code} is {field_comm};\n'
sql_insert = 'insert into {table_code}({fields}) values ({values});\n'

def build_insert(insert_data):
    fields = insert_data.fields
    cols = insert_data.cols
    table_code = insert_data.table_code
    insert_str = ''
    fields_str = ''
    for i in range(len(fields)):
        fields_str += str(fields[i]) + ','

    for i in range(len(cols)):
        values_str = ''
        for j in range(len(cols[i]) - 1):
            values_str += '\'' + str(cols[i][j]) + '\','

        insert_str += sql_insert.format(fields = fields_str[0:-1],
                                        values = values_str[0:-1],
                                        table_code = table_code)
    return insert_str

def build_table(tables):
    tables_str = ''

    for i in range(len(tables)):
        fields_str = ''
        comm_str = ''
        current_table = tables[i]
        current_fields = current_table.fields
        for j in range(len(current_fields)):
            current_field = current_fields[j]
            fields_str += sql_field.format(code = current_field.code,
                                           c_type = current_field.data_type,
                                           not_null = 'not null' if current_field.not_null != '' else '')
            comm_str += sql_field_comm.format(table_code = current_table.code,
                                              field_code = current_field.code,
                                              field_comm = current_field.name)
        tables_str += sql_table.format(table_code = current_table.code,
                                      fields = fields_str,
                                      pk_code = current_table.pk_code,
                                      field_comms = comm_str,
                                      table_name = current_table.name)

    return tables_str
