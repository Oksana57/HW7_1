import creat_contact1
import csv_creater
import import_book
import model


alist=import_book.import_book
contact1=import_book.import_book


def work_book():

    csv_creater.var_export()
    model.prompt()
    u=model.user_input()
    if u == 1:
        import_book.viewing_book()
    elif u == 2:
        model.add_file()
    elif u == 5:
        import_book.find_contact()
    elif u == 3:
        import_book.new_version()


work_book()
