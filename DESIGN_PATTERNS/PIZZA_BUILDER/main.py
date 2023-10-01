from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress','queue preparation baking ready')
PizzaDough = Enum('PizzaDough','thin thick')
PizzaSauce = Enum('PizzaSauce','tomato garlic_cream')
PizzaTopping = Enum('PizzaTopping','mozarella double_mozarella bacon ham mushrooms red_onion oregano')
STEP_DELAY = 3

class Pizza:
    def __init__(self,name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self,dough):
        self.dough = dough
        print(f'preparing the {self.dough.name} dough of Your {self}')
        time.sleep(STEP_DELAY)
        print(f'done with the {self.dough.name} dough.')


class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza('Margarita')
        self.progress = PizzaProgress.queue
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print(f'adding tomato sauce to Your Margarita!')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('Done with the tomato sauce!')

    def add_topping(self):
        topping_desc = 'podwójna mozarella, oregano'
        topping_items = (PizzaTopping.double_mozarella, PizzaTopping.oregano)
        print(f'adding the topping({topping_desc}) to Your Margarita!')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'Done with the topping({topping_desc})')

    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'baking Your Margarita for {self.baking_time} s')
        time.sleep(self.baking_time)
        print("Yor Margarita is ready!!!")
        
        
class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza('Creamy Bacon')
        self.progress = PizzaProgress.queue
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print(f'adding garlic_cream sauce to Your Creamy Bacon!')
        self.pizza.sauce = PizzaSauce.garlic_cream
        time.sleep(STEP_DELAY)
        print('Done with the garlic_cream sauce!')

    def add_topping(self):
        topping_desc = 'mozarella, boczek, szynka, grzyby, czerwona cebula, oregano'
        topping_items = (PizzaTopping.mozarella,
                         PizzaTopping.bacon,
                         PizzaTopping.ham,
                         PizzaTopping.mushrooms,
                         PizzaTopping.red_onion,
                         PizzaTopping.oregano)
        print(f'adding the topping({topping_desc}) to Your Creamy Bacon!')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'Done with the topping({topping_desc})')

    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'baking Your Creamy Bacon for {self.baking_time} s')
        time.sleep(self.baking_time)
        print("Yor Creamy Bacon is ready!!!")