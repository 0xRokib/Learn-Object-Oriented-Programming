class Wall:
    def __init__(self,armor,magic_resistance):
        self.__armor = armor
        self.__magic_resistance = magic_resistance
        
    def get_defence(self):
        return self.__armor + self.__magic_resistance
    
front_wall = Wall(10, 10)

print(front_wall.get_defence())
print(front_wall.__armor())
