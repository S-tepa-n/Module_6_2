class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, model: str, color: str, engine_power: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def sey_model(self):
        return (f'Модель:{self.__model}')

    def sey_engine(self):
        return (f'Мощьность двигателя: {self.__engine_power}')

    def sey_color(self):
        return (f'Цвет: {self.__color}')

    def print_info(self):
        print(self.sey_model())
        print(self.sey_engine())
        print(self.sey_color())
        print(f'Владелиц автомобиля: {self.owner}')

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя поменять цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()
