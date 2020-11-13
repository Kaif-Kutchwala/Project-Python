import pandas as pd
from openpyxl import *
import psycopg2

#Initialise Variables
global title
titles_found = False
counting_rows = True
skip_row = True
data = {}
row_count = 0
column_count = 0
table_name = 'logs_startimes'
columns = ['company_name', 'partner_name', 'transaction_no', 'status', 'customer_name', 'customer_address', 'amount', 'smartcard_no', 'phone', 'customer_code', 'creation_date', 'modification_date']

# Connect to Database (PostgreSQL)
conn = psycopg2.connect(database="portal", user = "postgres", password = "9503", host = "127.0.0.1", port = "5432")
cur = conn.cursor()


# Load Excel File
wb = load_workbook('C:\\Users\kaifk\Desktop\_\Rawbank\Report.xlsx')
ws = wb.active

# Scrape Data for Excel
for col in ws.iter_cols():
    titles_found = False
    skip_row = True
    for cell in col:
        if titles_found and cell.value != None:
            if skip_row:
                skip_row = False
            else:
                cell_value = str(cell.value).strip(' ="')
                if cell_value == 'Succès':
                    data[title].append(True)
                elif cell_value == 'Fail':
                    data[title].append(False)
                else:
                    data[title].append(cell_value)
                if counting_rows:
                    row_count += 1
        if not titles_found and cell.value != None and cell.value!= '':
            title = columns[column_count]
            data[title] = []
            titles_found = True
            column_count += 1
    counting_rows = False 

# Inset Data into table
insert_data = []
insert_string = 'INSERT INTO ' + table_name.lower() + ' ('
for title in data.keys():
    insert_string += title + ', '
else:
    insert_string = insert_string[:-2]
    insert_string += ') VALUES ('
for i in range(len(data.keys())):
    insert_string += '%s,'
else:
    insert_string = insert_string[:-1]
    insert_string += ')'

for i in range(row_count - 1):
    for key in data.keys():
        insert_data.append(data[key][i])
    cur.execute(insert_string, tuple(insert_data))
    #print(tuple(insert_data))
    insert_data.clear()

conn.commit()
count = cur.rowcount
cur.close()
conn.close()

        





