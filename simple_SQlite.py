

import sqlite3

ef handle_choice(choice):

    if choice == '1':
        input_data()

    elif choice == '2':
        search_data()

    elif choice == '3':
        delete_data()

    else choice == '4':
        msg()

    choice = input('Enter your selection: ')

    return choice




db = swlite3.connect('simple_sqlite_application') #Creates and opens database

cur.cursor()

cur.execute('Create table if not exists chainsaw_Record(Record_Holder text, country text, catches int)')
def input_data():
    name = input('Enter name: ')
    country = input('Enter country: ')
    catches = int(input('Rnter number of catches: '))
def add_new():
# provide data
    cur.execute('insert into chainsaw_Record values(?, ?, ?)', ( name, country,catches ))

#fetch data
def search_records():
    cur.execute('select*from simple_sqlite_application')
    for row in cur:
        print(row)

db.commit()

def main():
