from openpyxl import load_workbook

def open():
    exl = load_workbook('data.xlsx')
    list = exl['Лист1']
    id = []
    x = []
    y = []
    for i in range(1,129):
        val = list.cell(row=i+1, column=1).value
        id.append(val)
    for i in range (1, 129):
        val = list.cell(row=i+1, column=2).value
        x.append(float(val))
    for i in range (1, 129):
        val = list.cell(row=i+1, column=3).value
        y.append(float(val))
    return id, x, y


id, x, y = open()
coordinates = zip(y, x)
coordinates = list(coordinates)

