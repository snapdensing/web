import gspread

# Authentication
# - Replace filename argument with path to JSON credentials
gc = gspread.service_account(filename='./gsheets/sheets-api-282712-269669c1c437.json')

# Open file using URL key
sh = gc.open_by_key('1NKyqTGlKtnkMqlE40D97YI-ZSEeWVZIItUo8_kBstoE')

# Select worksheet
worksheet = sh.worksheet('Sheet3')

# Data to write, then read
data = [['Tadaka', 123],
        ['Kisada', 5810],
        ['Yokuni', 271],
        ['Mitsu', 8519],
        ['Shoju', 123]
       ]

print(data)
worksheet.update('A1', data)

# Find cell with value 'Yokuni'
cell = worksheet.find('Yokuni')
print('{} found at {},{}'.format(cell.value,cell.row,cell.col))

# Find cells with value 123
cell_list = worksheet.findall('123')
for item in cell_list:
  print('{} found at {},{}'.format(item.value,item.row,item.col))
