from dataclasses import dataclass,Field
from datetime import datetime

#Field -> 'default','dafault_factory','init','repr','hash','compare','metadata','kw_only'

params = {
    'firstname':Field(None,None,True,True,True,True,None,True),
    'lastname':Field(None,None,True,True,True,True,None,True),
    'year_of_birth':Field(None,None,True,True,True,True,None,True)
}

def age(self):
    return datetime.now().year - self.year_of_birth

MetaPerson = dataclass(type('MetaPerson',(),{'__annotations__':params,'age':property(age)}))

p = MetaPerson('Romulada','Tracz',1968)
print(p)
print(p.age)
