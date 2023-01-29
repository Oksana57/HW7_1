import import_book
import csv
import creat_contact1

import sys

key_of_book=import_book.key_of_book

means_of_book=import_book.means_of_book

book1=import_book.dict_book
contact1=import_book.import_book
alist=import_book.import_book


def prompt():
    
    print('Что вы хотите делать со справочником? ')
    menu_l=['посмотреть', 'дополнить', 'удалить', 'заменить', 'найти']
    for i, value in enumerate(menu_l, start=1):
        print(f'\t{i}, {value}')
    print()


def user_input():    
    n=int(input('выберете пункт меню: '))
    return n


def find_contact():
    number=input('Введите номер телефона для поиска')
    # if number in import_book.import_book:
    for i in book1:
        for j in i:
            if number in book1[i]:
                return 'Такой номер есть'
            else:
                return 'Такого номера нет'
   

def add_cont():
    book1 = creat_contact1.contact_input()
    # book=[]
    # while True:
    #     for i in range(1, 1000):
    #         c_surname = input('Введите фамилию абонента: ')
    #         c_name = input('Введите имя абонента: ')
    #         c_phone = input('Введите телефон: ')
    #         c_info = input('Введите описание: ')
    #         contact = [c_surname, c_name, c_phone, c_info]
    #         book.append(contact)
    #         print('хотите ввести еще? введите "да" или "нет": ')
    #         answer = input()
    #
    #         if answer == 'да':
    #             # dict2[i]=dict1
    #
    #             continue
    #
    #         elif answer == 'нет':
    #             break
    return book1

def book_for_rewrite():
    key1 = ['surname', 'name', 'phone', 'info']
    book_n = []
    contact1 = import_book.import_book()
    # contact = [c_surname, c_name, c_phone, c_info]
    dict1 = {key1[j]: contact1[j] for j in range(len(key1))}

    # contact1=' * '.join(contact)
    # dict2={}
    # dict2={i:dict1}
    book_n.append(dict1)
    # return contact1
    return book_n

print(book_for_rewrite())

def rewrite():
    book1 = book_for_rewrite()
    book2 = add_cont()
    book_rewrite = []
    book_rewrite = book1+book2

    return book_rewrite

# print(rewrite())


def book_new():
    contact2 = rewrite()
    key1 = ['surname', 'name', 'phone', 'info']
    dict2 = {}
    book = []
    for i in range(len(contact2)):
        dict2 = {key1[j]: contact2[i][j] for j in range(len(key1))}
        book.append(dict2)

    return book

def add_file():
    csv_file = 'data.csv'
    book = book_new()
    dict1 = book
    csv_columns = ['surname', 'name', 'phone', 'info']
    try:
        with open(csv_file, 'w') as file_c:
            writer=csv.DictWriter(file_c, fieldnames=csv_columns, delimiter="*")
            writer.writeheader()
            for data in dict1:
                writer.writerow(data)
    except IOError:
        print('I/O error')
    return


# add_file()



