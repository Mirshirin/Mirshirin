
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
class Mostatil:
    def __init__(self, a,b):
        self.tool=a
        self.araz=b
    def __repr__(self):
        return "mostatil with tool= %s  and araz=%s"%(self.tool,self.araz)
    def __gt__(self,other):
        return self.area() > other.area()
    def area(self):
        return self.tool * self.araz
    

m=Mostatil(1,5)
m1=Mostatil(1,3)
print(m)
print("mohseb is = " + str(m.area()))
print(m>m1)
if (m>m1):
    print("yes"+ "m > m1")
print("m =" +str(m.area()) +"   m1 ="+str(m1.area()) )
a = np.array([1,2,3])
print(a**2)
x=np.linspace(-1,1,10)
print(x)
print(np.sin(x))
data=pd.read_csv("Bo.csv")
print(data)
print(type(data))
print(data.iloc.__getitem__(0,0))

