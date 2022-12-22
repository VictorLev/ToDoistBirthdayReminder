from pandas import *
xls = ExcelFile('Birthday List.xlsx')
df = xls.parse(xls.sheet_names[0])

mylist = [df['name'].tolist(),df['date'].tolist()]

print (mylist)