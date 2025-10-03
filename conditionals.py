age= int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive')
elif age < 18:
   legal_age= 18-age
   print(f'You need {legal_age} years to learn to drive')
    
your_age = int(input('What is your age? '))
my_age = 20

if my_age < your_age:
   great_age = your_age - my_age
   print(f'You are {great_age} older than me')
elif my_age > your_age:
   less_age = my_age - your_age
   print(f'I am {less_age} older than you')
else:
   print('We are the same age')

number1 = int(input('Input a number: '))
number2 = int(input('Input another number: '))

if number1 > number2:
   print(f'{number1} is greater than {number2}')
elif number1 < number2:
   print(f'{number1} is smaller than {number2}')
else:
   print(f'{number1} is equal to {number2}')

score = int(input('Input your grades: '))
if score >=90 and  score <= 100:
   print('your grades is: A')
elif score >=70 and  score <= 89:
   print('your grades is: B')
elif score >=60 and score <=69:
   print('your grade is is: C')   
elif score >= 50 and score <= 59:
   print('your grade is: D')
elif score >=0 and score <= 49:
   print('your grade is: F')

print('Season Checker')
month_inputted = input('Input the month You want to check: ').strip().capitalize()

if month_inputted in ['September','October','November']:
   print(f'The month {month_inputted} is Autumn')
elif month_inputted in ['December','January','February']:
   print(f'The month {month_inputted} is Winter')
elif month_inputted in ['March','April','May']:
   print(f'The month {month_inputted} is Spring')
elif month_inputted in ['June','July','August']:
   print(f'The month {month_inputted} is Summer')
else:
   print(f'nigger are you stupid {month_inputted} aint a month')

fruits = ['banana','orange','mango','lemon']

User_fruits = input('Input a Fruit: ').strip().lower()
if User_fruits in fruits:
   print(f'The fruit {User_fruits} is already already exist in the list')
elif User_fruits not in fruits:
   fruits.insert(0,User_fruits)
   print(f'The fruit {User_fruits} is successfully added in the list')
   print (fruits)

me = {
    'first_name':'Frederick',
    'last_name': 'España',
    'age':'20',
    'Country':'Philippines',
    'is_broken':'Hell yeah',
    'skills':['Data Entry', 'Networking', 'C++', 'Sql', 'Python','JavaScript', 'React', 'Node', 'MongoDB','Linux'],
    'address':{
        'street':'Nigger Street',
        'zipcode':'1870',
    }
}

if 'skills' in me:
    middle_skill= me['skills'][4]
    print(f'The middle skill in skills is {middle_skill}')

if 'skills' in me and 'Python' in me['skills']:
    print('there is a Python in skills key')
else:
    print('there is no python in skills')

skills=set(me['skills'])
if skills == {'JavaScript','React'}:
    print('The skills he have are for a Front End Developer.')
if {'Node','Python','MongoDB'}.issubset(skills):
    print('The skills he have are for a Backend Developer.')
if {'React','Node','MongoDB'}.issubset(skills):
    print('The skills he have are for a Fullstack Developer')
if {'Sql','Data Entry'}.issubset(skills):
    print('The skills he have are for a Data Analyst')   
if {'Networking','Linux'}.issubset(skills):
    print('The skills he have are for A Cybersecurity Analyst')
else:
    print('Unkown Title') 

first_name=me['first_name']
last_name= me['last_name']
country= me['Country']   
if me['is_broken'] == 'False' and me['Country'] == 'Finland':
    print(f'{first_name} {last_name} lives in {country}. He is Married')
elif me['is_broken'] == 'Hell yeah' and me['Country'] == 'Philippines':
    print(f'{first_name} {last_name} lives in {country}. is he Broken by claire? {me["is_broken"]}')
     