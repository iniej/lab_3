

import sqlite3

db_name = 'chainsaw.db'

def main():

    # Why not set up your DB in the sqlite3 shell?

    while True:
        choice = get_choice()
        if choice == 'q':
            break
        if choice == '1':
            add_new()
        if choice == '2':
            show_all()
        if choice == '3':
            delete_record()
        if choice == '4':
            edit_records()
        if choice == '5':
            search_records()


        # etc.

def add_new():
    # get new data, call method to add to DB
    name = input('Enter name: ')
    catches = int(input('enter catches: '))
    country = input('Enter country: ')
    add_to_db(name, country, catches)


def add_to_db(name, country, catches):
    """ todo connect to db, insert data, handle errors """
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        make_table(db)
        cur.execute('insert into records values (?,?,?)', (name, country, catches))


def show_all():

    with sqlite3.connect(db_name) as db:
        for r in db.cursor().execute('select * from records'):
            print('Chainsaw juggler\'s name:  ' + r[0])
            print('Country: \t\t' + r[1])
            print('Number of catches:\t ' + str(r[2]) + '\n')


def make_table(db):
    cur = db.cursor()
    cur.execute('create table if not exists records ("Chainsaw juggling record Holder" text, Country text, "number of catches" int)' )

def delete_record():
    db = sqlite3.connect(db_name)
    cur = db.cursor()
    delete_name = input('Enter name: ')
    sqlite ='delete from records where "Chainsaw juggling record Holder" = ?'
    with  db:
        cur.execute(sqlite, (delete_name,))
        print('Data successfully deleted.')
            #print(delete_name + ' not found.')

def search_records():
    db = sqlite3.connect(db_name)
    cur = db.cursor()
    select_name = input('Enter name: ')

    sqlite ='select* from records where "Chainsaw juggling record Holder" = ?'
    with db:
        cur.execute(sqlite, (select_name,))
        for row in cur:
            print(row)

def edit_records():
    db = sqlite3.connect(db_name)
    cur = db.cursor()
    select_name = input('Enter name: ')
    num = int(input('Enter the number(an integer) of catches: '))
    sqlite = 'UPDATE records SET "number of catches" = ? WHERE "Chainsaw juggling record Holder" = ?'
    cur.execute(sqlite,(select_name,num))
        # for row in cur:
        #     print(row)
    db.commit()


def get_choice():

    print('''
    Press 1 to add new record
    Press 2 to show all records
    Press 3 to delete record
    Press 4 to edit record
    press 5 to search record
    Press q to quit program
    ''')
    return input('Enter choice: ')  # validation useful here.


main()
