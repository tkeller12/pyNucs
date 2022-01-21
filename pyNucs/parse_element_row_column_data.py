
with open('atomic_number_symbol_row_column.csv', 'r') as f:

    periodic_table_data = {}

    header_line = f.readline()
    header_list = header_line.strip().split(',')

    line = ''
    while True:

        line = f.readline()
        if line == '':
            break

        data = line.strip().split(',')

        info = {}
        for column, header in enumerate(header_list):
            info[header] = data[column]

        periodic_table_data[info['Symbol']] = info
print(periodic_table_data)
