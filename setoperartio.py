'''
Created on 01-May-2019

@author: jai
'''
days=set(["tue","wed","thu","fri","sat","sun"])
print(days)
days.add("jaya")
print(days)
py=set(["mon","tom","jam","fri"])
print(py)

days.discard("tue")
print(days)
qq=days
print(qq)

alldays=py|qq
print(alldays)

dd=py&qq
print(dd)

ee=py-qq
print(ee)