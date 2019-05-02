'''
Created on 01-May-2019

@author: jai
'''
jaya={1:"jaya",2:"ravi",3:"siva",4:"pavan",5:"ajay",6:"chinna",7:"suri"}
print(jaya)

a=jaya.keys()
print(a)

b=jaya.values()
print(b)

c=jaya.items()
print(c)

d=jaya.get(4,"empty")
print(d)

e=jaya.pop(2)
print(e)
print(jaya)

f={12:"ramesh"}

jaya.update(f)
print(jaya)

oo=jaya.items()
print(oo)

del jaya[1]
print(jaya)
