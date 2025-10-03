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
          


