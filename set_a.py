#!/usr/bin/env python3
#
# p. 89
#

"""
3.1 Create a string variable that is initialized to your entire name -
first, middle, and last.
"""
fname = 'Mason '
lname = 'Wing'
fullname = fname + lname
print(fullname)
"""
3.2 Using the slice operator, print your first name.
"""
print(fullname[0:6])
"""
3.3 Using the slice operator, print your last name.
"""
print(fullname[6:11])
"""
3.4 Using the slice and concatenation operators, print your name in the
form "Lastname, Firstname."
"""
print(fullname[6:11] + fullname[0:6])
"""
3.5 Print the length of your first name.
"""

print(len(fname))
"""
3.6 Assume you have two variables: `s='s'`, and `p='p'`. Using
concatenation and repetition, write an expression that produces the
string 'mississippi'.
"""
s ='s'
p = 'p'
m = 'm'
i = 'i'
print(m + (i + s + s) * 2 + i + p * 2 + i)
"""
3.7 Modify the prefix example in Session 3.5 to print all prefixes of
"Roy G Biv," including the entire string.
"""
def RGB():
    name = 'Roy G Biv'
    for i in range(len(name)):
        print(name[0:i+1])
print(RGB)
