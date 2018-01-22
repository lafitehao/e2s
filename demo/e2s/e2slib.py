class MyTable:
    _sql_main = 'drop table {table_code} cascade constraints;\n' +\
                   'create table {table_code}\n' +\
                   '(\n' +\
                   '{cols},\n' +\
                   'constraint PK_{table_code} primary key ({pk_code})\n' +\
                   ');\n' +\
                   'comment on table {table_code} is {table_name};\n' +\
                   '{col_comms}'
    _sql_col = '{code} {c_type} {not_null},\n'
    _sql_col_comm = 'comment on column {table_code}.{col_code} is {col_comm};\n'

    def __init__ (self, name, code):
        self.__name = name
        self.__code = code
        self.__cols = ''
        self.__pk_code = ''
        self.__col_comms = ''

    def set_pk (self, pk_code):
        self.__pk_code = pk_code

    def add_col (self, name, code, c_type, not_null):
        self.__cols += MyTable._sql_col.format (code = code,
                                         c_type = c_type,
                                         not_null = 'not null' if not_null != '' else '')
        self.__col_comms += MyTable._sql_col_comm.format (table_code = self.__code,
                                                   col_code = code,
                                                   col_comm = name)

    def build_table (self):
        return MyTable._sql_main.format(
            table_code = self.__code,
            table_name = self.__name,
            pk_code = self.__pk_code,
            cols = self.__cols[:-2],
            col_comms = self.__col_comms)
