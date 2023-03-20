from loguru import logger
from library import Library
from student import Student

def create_library():
    books = {
        'Gone with the wind': 'Free',
        'Python programing for every one': 'Free',
        'Clean code': 'Free',
        'Software design pattern': 'Free'
    }
    libr = Library(books)
    stud = Student('SuNT', libr)

    while True:
        logger.info('''
        ----------- LIBRARY FUNCTION MENU -------------
        1. Display available books
        2. Borrow a book
        3. Return a book
        4. View borrowed books
        5. Exit program
        ''')

        std_choise = int(input('Choise a function number: '))
        if std_choise == 1:
            libr.show_avail_books()
        elif std_choise == 2:
            stud.request_book()
        elif std_choise == 3:
            stud.return_book()
        elif std_choise == 4:
            stud.view_brrowed_books()
        else:
            exit()

if __name__ == '__main__':
    create_library()
