from dataclasses import dataclass
from collections.abc import Iterable
from typing import List

@dataclass
class Simple:
    field1:str
    field2:int

sp = Simple('abc',123456)
# for x in sp:
#     print(x)

print(isinstance(sp,Iterable))
print(isinstance([1,3,5,66,3],Iterable))

ds = Simple('jasio',55555)

print({'_'*50})

@dataclass
class Employee:
    firstname:str
    lastname:str
    accepted:bool = False

@dataclass
class Company:
    name:str

    def __post_init__(self):
        self._employees:List[Employee] = []

    def hire_employees(self,employee:Employee):
        self._employees.append(employee)

    def fire_employee(self,employee:Employee):
        self._employees.remove(employee)

    def __iter__(self):
        return iter(filter(lambda x:x.accepted,self._employees))

first_employee = Employee('Paweł','Kot',True)
second_employee = Employee('Olga','Knot',True)
third_employee = Employee('Olaf','Nowik')

company = Company('ABC')
company.hire_employees(first_employee)
company.hire_employees(second_employee)
company.hire_employees(third_employee)

for emp in company:
    print(emp)

company.fire_employee(first_employee)
print("usunięcie zasobu...")
for emp in company:
    print(emp)
