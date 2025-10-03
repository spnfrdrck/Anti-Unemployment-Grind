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
               