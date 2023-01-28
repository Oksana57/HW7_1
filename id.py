import csv
import sys

id=0

def get_ID():
    global id
    id+=1
    return id

def save_ID():
     global id
     with open ('id.txt', 'w', encoding='UTF-8') as file:
        file.write(str(id))

def get_from_file():
    global id
    with open ('id.txt', 'r', encoding='UTF-8') as file:
        file.read(int(id))


def import_book():
    with open('data.csv', encoding='UTF-8') as n_file:
        reader_object=csv.reader(n_file, delimiter="*")
        # data_list=csv.reader(n_file, delimiter="*") 
        for line in data_list:
            contact_info = line.strip().split(';')
            key_info = ['ID', 'Lastname', 'Firstname', 'phone', 'Comment']
            # dict_contact = dict(zip(key_info, contact_info))
            # add_in_contacts(dict_contact)



        # count=0
        # n=csv.field_size_limit(sys.maxsize)
        # for row in reader_object:
        #     if count==0:
        #         alist = ' '.join(row).split()
                   
                # print(f'Справочник содержит столбцы: {"| ".join(row)}')
            # elif 0<count<n:
                # line1=','.join(row).split()
                # line1=str(line1)
                # key=row[2]
                # line1=line1[0] + "," + line1[3:4]


            #     # contact1=' '.join(row).split()
            #     contact1.append(row)               
            # count+=1
            # if count==n:
            #     break
        #return alist, contact1
        # contact1
        # return dict_contact    
        # 
        # 
# book2=contact_input()
# print(book2)

# with open ('contact.txt', 'a', encoding='UTF-8' ) as file1:
#     file1.write(book2)
# def export(book2):
#     csv_columns = ['N','name', 'surname', 'phone', 'info']
#     dict=book2
#     csv_file='data.csv'
#     try:
#         with open(csv_file, 'w') as file_c:
#             writer=csv.DictWriter(file_c, fieldnames=csv_columns)
#             writer.writeheader()
#             for data in dict:
#                 writer.writerow(data)
#     except IOError:
#         print('I/O error') 

# export(book2)  
# 
# contact1=[] 
# with open('data.csv', 'r', encoding='UTF-8') as file1:
#         cont2=csv.reader(file1, delimiter="*")
#         count=0
#         n=csv.field_size_limit(sys.maxsize)
#         for row in cont2:
#             if count==0:
#             #     alist = ' '.join(row).split()
#                 count+=1
#                 continue 
#             if 0<count<n:           
#                 contact1.append(row)               
#             count+=1   

# print(contact1)   