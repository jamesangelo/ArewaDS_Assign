# -*- coding: utf-8 -*-
"""Variable.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TyZMbU4aul0Ngi62KWFenyPQufp7D8UP

#Exercise Level 1
"""

#Day 2: 30 Days of python programming

#3.
first_name = 'James'

#4.
last_name = 'Williams'

#5.
full_name = 'James Williams'

#6.
country = 'Sweden'

#7.
city = 'Vienna'

#8.
age = 16

#9.
year = 2024

#10.
is_married = True

#11.
is_true = True

#12.
is_light_on = True

#13.
x, y, z = 2, 'man', 3.9


# Exercise Level 2

#1.
print('first_name: ', type(first_name))
print('last_name: ', type(last_name))
print('full_name: ', type(full_name))
print('country: ', type(country))
print('city: ',type(city))
print('age: ',type(age))
print('year: ', type(year))
print('is_married: ', type(is_married))
print('is_true: ',type(is_true))
print(type(is_light_on))
print('x: ',type(x), 'y: ', type(y), 'z: ', type(z))

#2.
print(len(first_name))

#3
ln_lenght = len(last_name)
fn_lenght = len(first_name)
print('Fname > Lname :', fn_lenght > ln_lenght)
print('Fname < Lname :', fn_lenght < ln_lenght)
print('Fname == Lname :', fn_lenght == ln_lenght)

#4
num_one = 5
num_two = 4

#5
total = num_one + num_two

#6
diff = num_two - num_one

#7
product = num_two * num_one

#8
division = num_two / num_one

#9
reminder = num_two % num_one

#10
exp = num_one ** num_two

#11
floor_division = num_one//num_two

#12
#i
radius = 30
PI = 3.14
area_of_circle = PI * (radius ** 2)
print(area_of_circle)
#ii
circum_of_circle = 2 * PI * radius
print(circum_of_circle)
#iii
radius = int(input('Enter radius Val: ',))
area_of_circle = PI*(radius**2)
print(round(area_of_circle,2))

#13
first_name = input('Enter first name: ',)
last_name = input('Enter last name: ',)
country = input('Enter country: ',)
age = input('Enter age: ',)

#14
print(help('keywords'))