from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance

print("______________ klasa OldResistor _________________")
r0= OldResistor(10.2E2)
print(r0)
print(r0._ohms)
print(r0.get_ohms())
r0.set_ohms(2.88E3)
print(r0.get_ohms())

print("______________ klasa Resistor _________________")
r1 = Resistor(50.1E3)
print(r1.ohms)
r1.ohms = 1E2
print(r1.ohms)
print(f'układ elektryczny:\noporność: {r1.ohms} omów,\nnapięcie prądu: {r1.voltage} V,\n'
      f'natężenie prądu: {r1.current} A')


print("______________ klasa VoltageResistance _________________")
r2 = VoltageResistance(1E2)
print(f'natężenie początkowe prądu: {r2.current} A')
r2.voltage = 333
print(f'opór: {r1.ohms} omów')
print(f'napięcie prądu: {r2.voltage} V')
print(f'natężenie prądu: {r2.current} A')
