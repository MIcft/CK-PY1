OUTPUT_FILE = "output.csv"


def to_csv_file(filename, headers, rows, delimiter=',', new_line='\n') -> str:
    out = ""
    data_ = rows
    data_.insert(0, headers)
    for row in data_:
        for cell in row:
            out += cell
            if cell != row[-1]:
                out += delimiter
        out += new_line
    with open(filename, 'w', encoding='UTF-8') as file:
        for line_ in out:
            file.write(line_)



headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population',
                'households', 'median_income', 'median_house_value']
data = [
    ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500',
     '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000',
     '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400',
     '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900',
     '330000.000000'],
]

# TODO вызвать функцию to_csv_file и записать данные в файл
#
to_csv_file(OUTPUT_FILE, headers_list, data)
with open(OUTPUT_FILE) as output_f:
    for line in output_f:
        print(line, end="")
