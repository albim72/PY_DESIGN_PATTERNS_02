from abstract import AbstractFactory
from abstract_a import AbstractProductA
from abstract_b import AbstractProductB
from concrete_a import ConcreteProductA1,ConcreteProductA2
from concrete_b import ConcreteProductB1,ConcreteProductB2

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()
    
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()
