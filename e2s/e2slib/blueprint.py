class Table:
    def __init__(self, name = '', code = '', pk_code = ''):
        self.name = name
        self.code = code
        self.fields = []
        self.pk_code = pk_code

    def add_field(self, field):
        self.fields.append(field)

class Field:
    def __init__(self, name = '', code = '', data_type = '', not_null = ''):
        self.name = name
        self.code = code
        self.data_type = data_type
        self.not_null = not_null

class InsertData:
    fields = []
    cols = []

    def add_field(self, field_code):
        self.fields.append(field_code)

    def new_col(self):
        self.cols.append([])

    def last_col_append(self, value):
        self.cols[len(self.cols) - 1].append(value)

