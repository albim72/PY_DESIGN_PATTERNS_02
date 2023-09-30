from ocenaprojektu import Projekt

print('_________ klasa Projekt ______________')
g = Projekt()
g.grade = 97
assert g.grade == 97

print(f'ocena {g.grade}')
