import datetime

#1. Create a new class with some properties and methods

class Vehicle:
    def __init__(self, name, max_speed=100, color='red', year=2020) -> None:
        self.name = name
        self._max_speed = max_speed
        self.__color = color
        self.__year = year
    
    def get_name(self):
        return self.name

    def get_max_speed(self):
        return self._max_speed
    
    def get_color(self):
        return self.__color

    def __cal_yearold(self):
        year_old = datetime.datetime.now().year - self.__year
        return year_old

    def get_yearold(self):
        return self.__cal_yearold()

    def set_color(self, color):
        self.__color = color

    def set_max_speed(self, max_speed):
        self._max_speed = max_speed

# veh_o = Vehicle('Bicycle', 10, 'Green', year=2018)
# print(f'Max speed: {veh_o._max_speed}')
    
# 2. Create a Child class
class Motor(Vehicle):
    def __init__(self, name, engine, max_speed=100, color='red', year=2020) -> None:
        self.__engine = engine
        super().__init__(name, max_speed, color, year)

    def get_engine(self):
        return self.__engine

    def get_max_speed(self):
        # return super().get_max_speed() + 50
        return self._max_speed + 50


# Define a new object of child class
# motor_o = Motor('Air Blade', 150, max_speed=200, color='Black', year=2009)
# print('___________________ Motor Information ________________')
# print(f'Name: {motor_o.get_name()}')
# print(f'Color: {motor_o.get_color()}')
# print(f'Max_speed: {motor_o.get_max_speed()}')
# print(f'Year Old: {motor_o.get_yearold()}')
# print(f'Engine: {motor_o.get_engine()}')


''' 3. Define class Car which inherited from Vehicle.
- Add one more private property: Branch
- Add one more method to return branch information
- Overide method get_yearold(): add more one year-old for each Car
- Init a Car object, then print all information
'''    


'''
4. Polymorphism & Inheritance
'''
class Bird:
    def __init__(self) -> None:
        pass

    def intro(sefl):
        print('There are many types of birds here')

    def flight(self):
        print('Most of the bird can fly on the sky, some others can not')

    
class DaiBang(Bird):
    def __init__(self) -> None:
        super().__init__()

    def flight(self):
        print('Dai bang can fly')

class DaDieu(Bird):
    def __init__(self) -> None:
        super().__init__()

    def flight(self):
        print('Da dieu can not fly')
    

bird_o = Bird()
db_o = DaiBang()
dd_o = DaDieu()

# bird_o.intro()
# bird_o.flight()

# db_o.intro()
# db_o.flight()

# dd_o.intro()
# dd_o.flight()


#########################
# Polymorphism
class England:
    def capital(self):
        print('London is capital of England')

    def language(self):
        print('English is native language of England')

    def type_country(self):
        print('England is developed country')

class Vietnam:
    def capital(self):
        print('Hanoi is capital of Vietnam')

    def language(self):
        print('Vietnamese is native language of Vietnam')

    def type_country(self):
        print('Vietnam is developing country')
        

def func(obj):
    obj.capital()
    obj.language()
    obj.type_country()

england_o = England()
vn_o = Vietnam()
# for ct_o in [england_o, vn_o]:
#     func(ct_o)

# ###########
# def add(a, b, c=10):
#     return a+b+c

# add(2,3,4)
# add(2,3)
#####



'''
5. Abstraction
'''
from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def no_of_sides(self):
        pass

class Triangle(Polygon):
    # overide abstract method from parent class - mandatory
    def no_of_sides(self):
        print('The triangle has 3 sides')

class Hexagon(Polygon):
    def __init__(self) -> None:
        super().__init__()
    # def no_of_sides(self):
    #     print('The hexagon has 6 sides')

trg_o = Triangle()
trg_o.no_of_sides()

hxg_o = Hexagon()
hxg_o.no_of_sides()