# -*- coding: utf-8 -*-
"""set.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uvUYG9ugFMDtQfHiReJ2MRF1zp7HR-4m

# Sets Exercise Level 1
"""

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#1.
print('lenght of the set: ', len(it_companies))

#2.
it_companies.add('Twitter')
print(it_companies)

#3.
itcom = ('nvida', 'X', 'Yahoo')
it_companies.update(itcom)
print(it_companies)

#4.
it_companies.remove('Apple')

#5.
#remove method can only function when the item to remove is in the set of items
#howeveer, discard will not give a trace back error even if the item is not in the set

"""# Sets Exercises: Level 2"""

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#1.
A.union(B)
print(A)

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#2.
print(A.intersection(B))

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#3.

print('Is A subset of B:', A.issubset(B))

#4.
print('Is A and B disjoint: ', A.isdisjoint(B))

#5.
A.join(B)
B.join(A)

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#6.
print(A.symmetric_difference(B))

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

del A
del B

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


ages = set(age)
print(type(ages))
print('lenght of list > Set ? ', len(age) > len(ages))
print('lenght of list == Set ? ', len(age) == len(ages))
print('lenght of list < Set ? ', len(age) < len(ages))

"""# Sets Exercises: Level 3
# the difference between the different data types are shown below:

|String|List|Tuple|Set|
-------|----|-----|---|
|data is wrapped in ' ' or " "| data is wraped in square brackets with ',' separation| data is wrapped in brackets with ',' separation| data is wrapped in curly brackets|



"""

#3.
strin = 'I am a teacher and I love to inspire and teach people'
words = set(strin.split())
print(words)
print('There are ', len(words), ' unique words')