#!/usr/bin/env python3
#
# pp. 91, 93
#

"""
3.8 Using the count method, find the number of occurrences of the
character 's' in the string 'mississippi'.
"""
str = 'mississippi'
sub = 's' ;
print(str.count(sub, 0, 12))
"""
3.9 Replace all occurences of the substring 'iss' with 'ox'.
"""
str = 'mississippi'
print(str.replace('iss', 'ox'))
"""
3.10 Find the index of the first occurrence of 'p' in 'mississippi'.
"""
d = 'mississippi'
print(d.index('p'))
