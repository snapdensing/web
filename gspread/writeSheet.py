import gspread

# Authentication
# - Replace filename argument with path to JSON credentials
gc = gspread.service_account(filename='./gsheets/sheets-api-282712-269669c1c437.json')

# Open file using URL key
sh = gc.open_by_key('1NKyqTGlKtnkMqlE40D97YI-ZSEeWVZIItUo8_kBstoE')

# Select worksheet
worksheet = sh.worksheet('Sheet2')

# Writing using A1 notation
worksheet.update('A2','Hello')
val_A2 = worksheet.acell('A2').value
print('val_A2: {}'.format(val_A2))

# Writing using row/col coords
worksheet.update_cell(1,2,'World')
val_1_2 = worksheet.cell(1,2).value
print('val_1_2: {}'.format(val_1_2))

# Update a range
x = [[1,2], [3,4]]
worksheet.update('A3:B4', x)
values = worksheet.get_all_values()
print('All values:')
print(values)

