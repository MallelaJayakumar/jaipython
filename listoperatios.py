'''
Created on 30-Apr-2019

@author: jai
'''
a=[12,22,42,5,78,98,76,43]
a.append("$$$$")              
print(a)

a.pop(4)
print(a)

a.remove(5)
print(a)

a.extend([23,34])
print(a)

a.count(23)

a.insert(4,"hai")
print(a)

a.reverse()
print(a)

a.pop(2)
a.pop(4)
print(a)

a.sort()
print(a)

q=min(a)
print(q)

t=max(a)
print(t)