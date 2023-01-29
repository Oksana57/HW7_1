import csv
import sys


def import_book():
    # alist = []
    contact1 = []
    with open('data.csv', encoding='UTF-8') as n_file:
        reader_object=csv.reader(n_file, delimiter="*")
        count=0
        n=csv.field_size_limit(sys.maxsize)
        for row in reader_object:
            if count == 0:
                # alist = ' '.join(row).split()
                count += 1
                continue
            elif 0 < count < n:

                contact1.append(row)               
            count += 1
            if count == n:
                break
    return contact1

contact1=import_book()

# def book_for_rewrite():
#     key1 = ['name', 'surname', 'phone', 'info']
#     book_n = []
#     contact1 = import_book()
#     # contact = [c_surname, c_name, c_phone, c_info]
#     dict1 = {key1[j]: contact1[j] for j in range(len(key1))}
#
#     # contact1=' * '.join(contact)
#     # dict2={}
#     # dict2={i:dict1}
#     book_n.append(dict1)
#
#     return book


def key_of_book(contact1):
    key_of_book=[]
    for i in range(len(contact1)):
        for j in range(len(contact1[i])-3):
            key_of_book.append(contact1[i][2])
    return key_of_book

def means_of_book(contact1):
    means_of_book=[]
    for i in range(len(contact1)):
        for j in range(len(contact1[i])-3):
            n=contact1[i][0]           
            m=contact1[i][1]
            l=contact1[i][3]
            s=n + ', ' + m +', '+ l
            means_of_book.append(s)
    return means_of_book

def dict_book(key_of_book, means_of_book):
    book1=[]
    dict_book={}
    for k in range(len(key_of_book)):
        dict_book={key_of_book[k]: means_of_book[k]} 
        book1.append(dict_book)
    return book1     

# contact1=import_book()
print(contact1)
# print(type(contact1))
key1=key_of_book(contact1)
# print(key1)
means1=means_of_book(contact1)
# print(means1)
book1=dict_book(key1, means1)

# print(book1)

def viewing_book():
    alist=['name', 'surname', 'phone', 'info']
    print('|   ', ' | '.join(alist), '  |')
    contact1=import_book()
    for i in range(len(contact1)):
        for j in range(len(contact1[i])):
            view1='--'.join(contact1[i])
        # print('|', '|'.join(alist), '|')
        print('|', view1, '|')
    return

# print(viewing_book())

def find_contact():
    number=input('Введите номер телефона для поиска: ')
    # if number in import_book.import_book:
    # for i in range(len(ali)):
        # for j in range(len(book1[i])):
    if number in key1:
        return print('Такой номер есть')
    else:
        return print('Такого номера нет')
    

def user_number():
    number=input('Введите номер телефона для удаления контакта: ')
    return number


def del_contact():
    number=user_number()
    contact1=[]
    with open('data.csv', 'r', encoding='UTF-8') as file1:
        cont2=csv.reader(file1, delimiter="*")
        count=0
        n=csv.field_size_limit(sys.maxsize)
        for row in cont2:
            if count==0:
            #     alist = ' '.join(row).split()
                count+=1
                continue 
            if 0<count<n:           
                contact1.append(row)               
            count+=1
        n=len(contact1)-1
        # len(contact1[i]
        for i in range(0,n+1):
            for j in range(len(contact1[i])):
                if number==contact1[i][j]: 
                    del contact1[i]
                    n=n-1
                    i=i-1
               
     
    return contact1   
# contact2=del_contact()
# print(contact2)

def book_new():
    contact2=del_contact()
    key1=['name', 'surname', 'phone', 'info']
    dict2={}
    book=[]
    for i in range(len(contact2)):
        dict2 = {key1[j]: contact2[i][j] for j in range(len(key1))}
        book.append(dict2)   
    
    return book

# book=book_new()
# print(book)

def new_version():
    book=book_new()
    dict=book
    csv_columns = ['surname', 'name', 'phone', 'info']
    csv_file='data.csv'
    try:
        with open(csv_file, 'w') as file_c:
            writer=csv.DictWriter(file_c, fieldnames=csv_columns, delimiter="*")
            writer.writeheader()
            for data in dict:
                writer.writerow(data)
    except IOError:
        print('I/O error')  
    return

# new_version()