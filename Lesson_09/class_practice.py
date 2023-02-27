class Student:
    def __init__(self, name_, age_, address_, mobile_number_):
        self.__name = name_
        self.__age = age_
        self.__address = address_
        self.__mobile_number = mobile_number_
    
    def __get_student(self):
        print(f'Student information:')
        print(f'Name: {self.__name}')
        print(f'Age: {self.__age}')
        print(f'Address: {self.__address}')
        print(f'Mobile Phone: {self.__mobile_number}')
        
    def set_student(self, name_, age_, address_, mobile_number_):
        self.name = name_
        self.age = age_
        self.address = address_
        self.mobile_number = mobile_number_

    def study(self, subject_name):
        print(f'I am studying {subject_name}!')

    def watch_movie(self, movie_name):
        print(f'I am watching my favourite movie {movie_name}!')

# std_1 = Student('Mai Anh', 19, 'Thai Binh', '0987684765')
# std_1.get_student()
# print('---------- New Informations ------------')
# std_1.set_student('SuNT', 20, 'Ha Noi', '0988783489')
# std_1.get_student()
# print('---------- New Informations ------------')
# std_1.set_student('Duc Nam', 28, 'Ha Noi', '0988783489')

# std_1.study('Math')
# std_1.watch_movie('Titanic')

std_2 = Student('Tung Lam', 39, 'Nghe An', '88888888')
# print(f'Name of student: {std_2.__name}')
# print(f'Age of student: {std_2.__age}')
# print(f'Address of student: {std_2.__address}')
# print(f'Mobile number of student: {std_2.__mobile_number}')
std_2.__get_student()