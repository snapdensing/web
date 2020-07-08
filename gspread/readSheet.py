import gspread

# Authentication
# - Replace filename argument with path to JSON credentials
gc = gspread.service_account(filename='./gsheets/sheets-api-282712-269669c1c437.json')

# Open file using URL key
sh = gc.open_by_key('1NKyqTGlKtnkMqlE40D97YI-ZSEeWVZIItUo8_kBstoE')

# Select worksheet
worksheet = sh.worksheet('Sheet1')

# Read using row/col coordinates
val_1_1 = worksheet.cell(1,1).value
val_2_2 = worksheet.cell(2,2).value
print('val_1_1: {}'.format(val_1_1))
print('val_2_2: {}'.format(val_2_2))

# Read using A1 notation
val_A1 = worksheet.acell('A1').value
val_B2 = worksheet.acell('B2').value
print('val_A1: {}'.format(val_A1))
print('val_B2: {}'.format(val_B2))

# Read entire Row
valrow_1 = worksheet.row_values(1)
print('valrow_1: {}'.format(valrow_1))
print('valrow_1 type: {}'.format(type(valrow_1)))

# Read entire Col
valcol_2 = worksheet.col_values(1)
print('valcol_2: {}'.format(valcol_2))
print('valcol_2 type: {}'.format(type(valcol_2)))

# Read all values and store to a list of lists
values = worksheet.get_all_values()
print('values:')
print(values)


