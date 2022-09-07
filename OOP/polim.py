class Phone:

    def __init__(self):
        self.is_on = False

    # Включаем телефон
    def turn_on(self):
        pass

    # Если телефон включен, делаем звонок
    def call(self):
        pass

    # Метод который выводит короткую сводку по классу Phone
    def info(self):
        print(f'Class name: {Phone.__name__}')
        print(f'If phone is ON: {self.is_on}')


# Унаследованный класс
class MobilePhone(Phone):

    # Добавляем новое устройство battery
    def __init__(self):
        super().__init__()
        self.battery = 0

    # Такой же метод, который выводит короткую сводку по классу MobilePhone
    # Обратите внимание, что названия у методов совпадают - оба метода называются info()
    # Однако их содержимое различается
    def info(self):
        print(f'Class name: {MobilePhone.__name__}')
        print(f'Is mobile phone is ON: {self.is_on}')
        print(f'Battery level: {self.battery}')

    # Демонстрационная функция
    # Создаем список из классов
    # В цикле перебираем список и для каждого элемента списка(а элемент- это класс)
    # Создаем объект и вызываем метод ihfo()
    # Главная особенность: запись object.info() не дает информацию об объекте, для которого будет вызван метод info()
    # Это может быть объект класса Phone, а может - объект класса MobilePhone
    # И только в момент исполнения когда становится ясно, для какого именно объекта нужно вызывать метод info()


def show_polymorfism():
    for item in [Phone, MobilePhone]:
        print('--------')
        object = item()
        object.info()
        

show_polymorfism()
