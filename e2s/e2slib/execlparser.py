from . import blueprint

def parse_data(sh):
    sh = sh
    data = blueprint.InsertData()

    for i in range(sh.nrows):
        if sh.cell_value(i, 0) == 0:
            for j in range(sh.ncols):
                data.add_field(sh.cell_value(i, j))
        else:
            data.new_col()
            for j in range(1, sh.ncols):
                data.last_col_append(sh.cell_value(i, j))

    return data

def parse_table(sh):
    sh = sh
    tables = []

    for i in range(1, sh.nrows):
        if sh.cell_value(i, 0) == 0:
            tables.append(blueprint.Table(sh.cell_value(i, 1), sh.cell_value(i, 2)))
        elif sh.cell_value(i, 0) != '' :
            last_table = tables[len(tables) - 1]
            last_table.add_field(
                blueprint.Field(sh.cell_value(i, 1), sh.cell_value(i, 2),
                                sh.cell_value(i, 3), sh.cell_value(i, 4)))
            if sh.cell_value(i, 5) != '':
                last_table.pk_code = sh.cell_value(i, 2)

    # 确保主键存在
    for i in range(len(tables)):
        current_table = tables[i]

        if current_table.pk_code == '':
            current_table.pk_code = current_table.fields[0].code
    return tables
