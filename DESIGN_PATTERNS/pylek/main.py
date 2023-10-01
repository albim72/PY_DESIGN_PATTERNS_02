import random
from enum import Enum

CarType = Enum('CarType','subcompact compact SUV')

class Car:
    pool = dict()
    def __new__(cls,car_type):
        obj = cls.pool.get(car_type,None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[car_type] = obj
            obj.car_type = car_type
        return obj
    
    def render(self,color,x,y):
        type = self.car_type
        msg = f'reneder a car type {type} and {color} at ({x},{y})'
        print(msg)
        
def main():
    
