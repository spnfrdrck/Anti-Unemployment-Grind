for number in range(11):
    print(number)

number = 0   
while number < 11:
    print(number)
    number= number+1
    
count= 0
hashtag = '#'
while count < 7:
    print(hashtag)
    hashtag += '#'
    count += 1


rows = 8 
column = 8

for i in range(rows):
    for j in range(column):
        print('*', end='')
    print()

num1 = 0
num2= 0
product = num1 * num2

for i in range(11):
    print (f'{num1} x {num2} = {product}')
    num1 +=1
    num2 +=1 
    product = num1 * num2

language= ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in language:
    print(item)   

for i in range(101):
    if i % 2:
        print (f'{i} is an even number')
        
for i in range (101):
    if i %2 != 0:
        print (f'{i} is an odd number') 
           
for i in range(101):
    if i % 2:
        print (f'{i} is an even number')
    else:
        print(f'{i} is an odd number')  

start = 0
for i in range(1,101):
    start += i
    print (start)

odd = 0
even= 0
for i in range (101):
    if i %2 == 0:
        even += i
    else:     
        odd +=i
print (f'The sum of even numbers is {even}. While the sum of odd numbers is {odd}')

countries = [
    "Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Canada","Cape Verde","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo","Costa Rica","Croatia",
    "Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini","Ethiopia","Fiji","Finland","France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Ivory Coast",
    "Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Korea (North)","Korea (South)","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar","Namibia","Nauru","Nepal","Netherlands","New Zealand",
    "Nicaragua","Niger","Nigeria","North Macedonia","Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russia","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Sweden","Switzerland","Syria",
    "Taiwan","Tajikistan","Tanzania","Thailand","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","Uruguay","Uzbekistan","Vanuatu","Vatican City","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"
]
for country in countries:
    if 'land' in country:
        print(country)

fruits = ['banana', 'orange', 'mango', 'lemon'] 
for fruit in reversed(fruits): 
    print(fruit)
    
import urllib.request, json

url = "https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/countries-data.py"
response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")

countries = json.loads(data)

unique_languages = set()
for country in countries:
    for lang in country['languages']:
        unique_languages.add(lang) 

print('Total number of unique Languages: ',len(unique_languages))    

counts = {}

for country in countries:
    for lang in country['languages']:   
        if lang in counts:
            counts[lang] += 1
        else:
            counts[lang] = 1

most_common = max(counts, key=counts.get)
most_common_value =  (counts[most_common])  
print('The most common language is', most_common, 'with', most_common_value, 'countries')

population_count = {}

for country in countries:
    population = country['population']   
    population_count[country['name']] = population

top10_populated = sorted(population_count, key=population_count.get, reverse=True)[:10]

print('The 10 most populated countries are:', top10_populated)
