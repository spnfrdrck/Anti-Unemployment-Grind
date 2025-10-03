front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)

full_stack = front_end
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print (full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min = (min(ages))
max = (max(ages))
print (min)
print (max)
ages.append('19')
ages.append('26')
print (ages)

ages = list(map(int,ages))
def median():
    medians = (ages[5] + ages[6])/2
    print(f"the median is: {medians}")

def average_age():
    average =sum(ages) / len(ages)
    print(f"The Average is {average}")

def range_of_num():
    range = max - min
    print(f"The range is: {range}")
    
def compare():
    average =sum(ages) / len(ages)
    compare_min= abs(min- abs(average))
    compare_max= abs(max - abs(average))
    print(f"The compared value of maximum is {compare_max}, while the minimum is {compare_min}")
    
median()
average_age()
range_of_num()
compare()
empty_list = []
if not empty_list:
  print('empty')

crush = ["athena","ali","yanna","claire","ysabel"]
print(len(crush))
print(crush [0])
print(crush [2])
print(crush [4])

mixed_data_types = ['Fred','20','172cm','waiting for my LOML','Annex 2 Lot 4 Brittany 1']
it_companies = ['Facebook','google','microsoft','apple','IBM','oracle','Amazon']
print(mixed_data_types,it_companies)
no_company= (len(it_companies))
print(no_company)
it_first = it_companies[0]
it_mid= it_companies[3]
it_last = it_companies[6]

print(it_first,it_mid,it_last)

it_companies[0] = 'Adobe'
it_companies[1] = 'Cisco'
it_companies[3] = 'Tencent'

print (it_companies)

it_companies.append('Alibaba')
it_companies.insert(2,'NVIDIA')
print(it_companies)

it_companies[8] = 'ALIBABA'
print(it_companies)

all_list = it_companies + mixed_data_types
print(all_list)

all_list.extend(mixed_data_types)
all_list.extend(it_companies)
print(all_list)

for IBM in all_list:
  print('there is IBM')
  print(all_list.count('IBM'))

all_list.sort()
print(all_list)

all_list.sort(reverse=True)
print(all_list)

all_list_spliced_1st_half = all_list[0:3]
print (all_list_spliced_1st_half)

all_list_spliced_last_half = all_list [-3:]
print(all_list_spliced_last_half)

all_list.remove('172cm')
all_list.remove('oracle')
print(all_list)

all_list.clear
print (all_list)         


