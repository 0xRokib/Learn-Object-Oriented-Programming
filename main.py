# 

# class Wall:
#     def __init__(self,height):
#         self.__height = height
        
#     def get_height(self):
#         return self.__height
    
# class Castle(Wall):
#     def __init__(self,height,towers):
#         super().__init__(height)
#         self.towers = towers
        
#     def get_tower_height(self):
#         return self.get_height() * 2


class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if self.__num_arrows <= num:
            raise Exception('not enough arrows')
        self.__num_arrows -= num

class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
       self.use_arrows(3)
       return f'{target.get_name()} was shot by 3 crossbow bolts'
        
