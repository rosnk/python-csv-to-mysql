This python is to insert bulk mysql data from csv file

Prerequisit:
mysql schema needs to be in place.

Uses:
replace path to .csv
with open('/path/to/file.csv', 'r') as csvfile:

replace table_name with mysql table name
replace table field name in place of field1,field2 and corrosponding %s,%s

cursor.executemany(
'INSERT INTO table_name (field1,field2) VALUES (%s,%s)',
data
)
