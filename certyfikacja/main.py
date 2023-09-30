from ocenaprojektu import Projekt
from exam_grade import Exam

print('_________ klasa Projekt ______________')
g = Projekt()
g.grade = 97
assert g.grade == 97

print(f'ocena {g.grade}')

print('_________ klasa Exam ______________')
e1 = Exam()
e1.first_part = 34
e1.second_part = 49
e1.third_part = 12

print(f'egzamin -> pierwsze podejście -> 1: {e1.first_part}, 2: {e1.second_part}, 3:{e1.third_part}')

e2 = Exam()
e2.first_part = 51
e2.second_part = 76
e2.third_part = 48

print(f'egzamin -> drugie podejście -> 1: {e2.first_part}, 2: {e2.second_part}, 3:{e2.third_part}')

print(f'dane z archiwum -> 1 podejście...')

print(f'egzamin -> pierwsze podejście -> 1: {e1.first_part}, 2: {e1.second_part}, 3:{e1.third_part}')
