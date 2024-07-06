class Vehicle:
    def __init__(self,owner, __model,__color,__engine_power,):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color =__color
        self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        return f' Модель: {self.__model}\n'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}\n'

    def get_color(self):
        return f'Цвет: {self.__color}\n'

    def print_info(self):
        print(self.get_model(),self.get_horsepower(),self.get_color(),f'Владелец: {self.owner}')

    def set_color(self,new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')






class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()

