# def add_num(num1,num2):
#     sum = num1 + num2
#     return sum

# print(add_num(69,67))

# import math
# def area_of_circle(radius):
#     area = math.pi * radius **2
#     return area
# print(area_of_circle(169))
    

# def add_all_num(*nums):
#     total = 0
#     for num in nums:
#         if isinstance(num, (int,float)):
#             total += num
#         else:
#             print(num, 'is not a number')
#     return total
# print(add_all_num(24,69,87,67,69,69.999,69.67,69.696768,'nigger ka wayne di mo sinabi mali kami'))

# def temp_converter(C):
#     Fahrenheit = (C * 9/5)+32
#     return (Fahrenheit,'Fahrenheit is the conversion from', C, 'Celsius')
# print(temp_converter(67))

# def check_season(month):
#     month = month.capitalize()
#     summer = ["June", "July", "August"]
#     autumn = ["September", "October", "November"]
#     winter = ["December", "January", "February"]
#     spring = ["March", "April", "May"]
    
#     if month in summer:
#         return (f'The {month} is summer')
#     elif month in autumn:
#         return ((f'The {month} is autumn'))
#     elif month in winter:
#         return ((f'The {month} is winter'))
#     elif month in spring:
#         return ((f'The {month} is spring'))
# print(check_season('august'))

# def slope_calculator(x1,x2,y1,y2):
#     slope = (y2-y1)/(x2-x1)
#     return(f'The slope is {slope:.2f}')
# print(slope_calculator(69,67,96,97))

# def slope_calculator_better():
#     user_pair1 = input('Type two numbers for ordered pair (x1 y1): ').split(',')
#     user_pair2 = input('Type another two numbers for ordered pair (x2 y2): ').split(',')
    
#     ordered_pair1 = [int(num) for num in user_pair1]
#     ordered_pair2 = [int(num) for num in user_pair2]
    
#     x1, y1 = ordered_pair1
#     x2, y2 = ordered_pair2
    
#     slope = (y2 - y1) / (x2 - x1)
    
#     return f'The slope for {ordered_pair1} \n and {ordered_pair2} is {slope}'

# print(slope_calculator_better())

# import sympy as sp
# def quadriatic_equation(a,b,c):
#     x = sp.symbols('x')
#     expr = a*x**2 + b*x + c
#     factored_expr = sp.factor(expr)
#     quad_x = sp.solve(factored_expr,x)
#     return  quad_x
# print(quadriatic_equation(2,6,12))
    
# def reverse_list(*nums):
#     num_list = list(nums)
#     reverse_list=[]
    
#     for num in range(1,len(num_list)+1):
#         reverse_list.append(num_list[-num]) 
#     return reverse_list
# print(reverse_list(1,2,3,4,67,89,27,9,12))
    
# def reverse_list_meonly(*nums):
#     num_list = list(nums)
#     reverse_list = list(reversed(num_list))
#     return reverse_list
# print(reverse_list_meonly(1000,10,10101001,101020,0,21021021,21212,344,3,44,434,34,3435566,566,76,77,6))  
    
# def capitalize_list_items(*item):
#     item_list = list(item)
#     capitalize_list_items=[]
#     for item in item_list:
#         capitalize_list_items += [item.capitalize()]
#     return capitalize_list_items
# print(capitalize_list_items('mango','banana','pepe','tite','sex','lube','condom'))

# foods=['fried chicken','roast beef','beef wellington','steak']
# def add_list(foods,*add_food):
#   total_item = []
#   for item in foods:
#     total_item.append(item)
#   for item in add_food:
#       total_item.append(item)
#   return total_item
# print(add_list(foods,'caldereta','patatim','lechon kawali'))
  

# def add_listpt2(foods,*add_food):
#    added_food= []
#    for item in add_food:
#       added_food.append(item)
#       total_food = foods+list(add_food)
#    return total_food  
# print(add_listpt2(foods,'tinola','mechado','adobo'))


# def remove_item(foods,*remove):
#    remove_list=list(remove)

#    for item in remove_list:
#       if item in foods:
#          foods.remove(item)
#       return(foods)
# print(remove_item(foods,'steak','roast beef'))

# def sum_of_numbers(number):
#    sum = 0
#    for i in range (number+1):
#        sum += i
#    return sum
# print(sum_of_numbers(10))

# def sum_of_odds(number):
#    odds_sum = 0 
#    for i in range(number+1):
#       if i %2 != 0:
#          odds_sum += i
#    return odds_sum

# print(sum_of_odds(69))
   
# def sum_of_even(number):
#    even_sum = 0 
#    for i in range(number+1):
#       if i %2 == 0:
#          even_sum += i
#    return even_sum

# print(sum_of_even(69))

# def even_and_odds(positive):
#   for i in range(positive+1):
#     if i % 2 == 0:
#       print (f'{i} is a even number')
#     else:
#       print(f'{i} is a odd number')
# print(even_and_odds(1000))

# def factorial(whole):
#   if not isinstance(whole,int) or whole <0:
#     return 'only fucking whole numbers bitch'
#   for i in range (1,whole +1):
#     whole *= i
#   return (whole)

# print(factorial(10))

# my_wallet = []
# my_heart =['claire','athena','ali','ara']
# def is_empty(check):
#   if len(check) == 0:
#     return 'the list is empty'
#   else:
#     return 'the list has something in it'
# print(is_empty(my_wallet))

numbers = [12, 45, 67, 89, 23, 56, 78, 90, 34, 21, 65, 87, 43, 32, 10]
def mean (numbers):
  sum = 0
  for i in numbers:
    sum+=i
  mean = sum / len(numbers)
  return f'The mean of the number list is: {mean}'

def median(numbers):
    sorted_number = sorted(numbers)
    n = len(sorted_number)
    if n % 2 == 0: 
        mid1 = sorted_number[n//2 - 1]
        mid2 = sorted_number[n//2]
        median = (mid1 + mid2) / 2
    else:  
        median = sorted_number[n//2]
    return f'The median for the number list is: {median}'


def mode(numbers):
   counts={}
   for i in numbers:
     if i in counts:
      counts[i] = counts[i]+1
     else:
      counts[i] = 1
   return max(counts, key=counts.get)


def variance(numbers):
  add = 0
  for i in numbers:
    add+=i
  mean = add / len(numbers)
  variance = sum((add-mean)**2 for x in numbers) /len(numbers)
  return f'The variance of the number list is: {variance:.2f}'

import math
def std(numbers):
  add = 0
  for i in numbers:
    add+=i
  mean = add / len(numbers)
  variance = sum((x-mean)**2 for x in numbers) /len(numbers)
  std = math.sqrt(variance)
  return f'The standard deviation of number list is: {std:.2f}'

print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(variance(numbers))
print(std(numbers))

#level 3
# def prime(number):
#     is_prime = True   
#     for i in range(2, number):
#         if number % i == 0:   
#             is_prime = False
#             break   
    
#     if is_prime:
#         print(f"The {number} is prime number")
#     else:
#         print(f"The {number} is composite")
# print(prime(27))

# unique_desserts = [
#     "ice cream","cheesecake","brownie","apple pie","chocolate cake",
#     "panna cotta","tiramisu","donut","macaron","cupcake"
# ]

# duplicate_desserts = [
#     "ice cream","cheesecake","brownie","apple pie","ice cream",       
#     "tiramisu","donut","macaron","brownie","cupcake"
# ]

# def unique_item_checker(Item_list):
#     unique = True
#     checked=[]
#     for item in Item_list:
#         if Item_list.count(item)> 1 and item not in checked:
#             unique = False
#             print(f'the dessert {item} is not unique')
#             checked.append(item)
            
#     if unique:
#         print('The list is unique')
#     else:
#         print('The list is not unique')
# print(unique_item_checker(duplicate_desserts))

# same_type_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# different_type_list = [1, "apple", 3.14, True, 42, "banana", 7.77, False, "cake", 100]
        
# def unique_type_checker(item_list):
#     first_type = type(item_list[0])
#     unique = True
#     checked = []
    
#     for item in item_list:
#         if type(item) != first_type:
#             checked.append(type(item))
#             print(f'The item "{item}" has type {type(item).__name__}, '
#       f'but expected {first_type.__name__}')

#             unique = False
#             break
#     if unique:
#         return 'The list has the same data type'
#     else:
#         return 'The list has different data types'
# print(unique_type_checker(different_type_list))
            
import keyword

def valid_variable(var):
    if isinstance(var,str) and var.isidentifier() and not keyword.iskeyword(var):
         return f'{var} is a valid Python variable'
    else:
        return f'{var} is not a valid python variable'
print(valid_variable('pussymagnet-69'))
               