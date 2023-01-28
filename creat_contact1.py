import csv



print('Давайте заполним телефонный справочник')

def contact_input():
    book=[]
    # dict2={}
    while True:
        for i in range(1,1000):
        
            c_surname=input('Введите фамилию абонента: ')
            c_name=input('Введите имя абонента: ')
            c_phone=input('Введите телефон: ')
            c_info=input('Введите описание: ')
            # dict1={}
            key1=['name', 'surname', 'phone', 'info']

            contact=[c_surname, c_name, c_phone, c_info]
            dict1 = {key1[j]: contact[j] for j in range(len(key1))} 
           
            # contact1=' * '.join(contact)
            # dict2={}
            # dict2={i:dict1}
            book.append(dict1)
            print('хотите ввести еще? введите "да" или "нет": ')
            answer=input()

            if answer=='да':
                # dict2[i]=dict1
               
                continue
                # while True:
                #     dict2={i:dict1}
                
                #     continue
            elif answer=='нет':

        
                # dict2={i:dict1}
                break
        # return book
        
        return book



        