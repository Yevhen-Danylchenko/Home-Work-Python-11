class Appliance:
    def __init__(self, brand):
        self.brand = brand
    def get_info(self):
        print(f'{self.brand}')

class KitchenAppliance(Appliance):
    def __init__(self, brand, power):
        super().__init__(brand)
        self.power = power
    def get_info(self):
        print(f'{self.brand}, {self.power}')

class Oven(KitchenAppliance):
    def __init__(self, brand, power, temperature_range):
        super().__init__(brand, power)
        self.temperature_range = temperature_range
    def get_info(self):
        print(f'{self.brand}, {self.power}, {self.temperature_range}')

class Microwave(KitchenAppliance):
    def __init__(self, brand, power, capacity):
        super().__init__(brand, power)
        self.capacity = capacity
    def get_info(self):
        print(f'{self.brand}, {self.power}, {self.capacity}')

obj = Oven('Borsh', 3, 30)
obj1 = Microwave('LG', 1.5, 300)

obj.get_info()
obj1.get_info()