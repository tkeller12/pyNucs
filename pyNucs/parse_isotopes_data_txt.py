
with open('isotopes_data.txt', 'r') as f:

    elements = {}

    header_line = f.readline()
    header_list = header_line.strip().split('\t')
    print(header_list)

    while True:
        isotope = {}
        line = f.readline()
        if line == '':
            break
        data = line.strip('\n').split('\t')
        print(data)
        for column, header in enumerate(header_list):
#            print(column)
#            print(header)
            isotope[header] = data[column]

        if isotope['Symbol'] not in elements:
            elements[isotope['Symbol']] = []

        elements[isotope['Symbol']].append(isotope)
print(elements)
print(elements['H'][0]['Spin'])
print(elements['H'][0]['Line-width Factor (l/fm^4)'])
print(elements['H'][0]['Relative Receptivity 1H'])
