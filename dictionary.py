dog={
  'name':'Susan',
  'color': 'Desaturated Dark Orange',
  'breed':'Corgi',
  'legs':'4 legs',
  'age':'14 years old'
}

student={
  'first_name':'Frederick',
  'last_name':'España',
  'gender':'Alpha Male',
  'age':'20 years old',
  'marital_status':['single','yearning','SEX','gusto na magmahal'],
  'skills':['Beginner python','beginner C++','Beginner networking','beginner Trader'],
  'country':'Philippines',
  'city': 'Antipolo City',
  'Address':'Annex 2 Lot 4 Brittany 1 Executive Homes, Brgy. San Isidro'
}

len_of_students = (len(student))
print(f'The length of Student Dictionary is {len_of_students}')

values_skill = student['skills']
print(values_skill)
print(type(values_skill))

student['skills'].append('HTML')
student['skills'].insert(3,'Basketball')

print(student['skills'])

print(student.keys())
print(student.values())
print(student.items())

del student['skills']
student.popitem()
student.pop('marital_status')

print(student)

del student
print (student)
print(dog)