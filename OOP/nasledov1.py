#Создаем класс Vehicle
class Vehicle:
    def vehicle_method(self):
        print('Это родительский метод из класса Vehicle')
#Создаем класс Car, который наследует Vehicle
class Car(Vehicle):
    def car_method(self):
        print('Это дочерний метод из класса Car')
#Создаем класс Cicle, который наследует Vehicle
class Cycle(Vehicle):
    def cycle_method(self):
        print('Это дочерний метод из класса Cycle')

car_a = Car()
car_a.vehicle_method() # вызов метода родительского класса
car_b = Cycle
car_b.vehicle_method() # Вызов метода родительского класса