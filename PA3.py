# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 13:20:26 2024

@author: JPMarschall
"""

import numpy as np

#%%
firstFunc = np.poly1d([2,3,0,1])
print(firstFunc)
evalFunc = np.polyval(firstFunc,2)
print(evalFunc)

secondFunc = np.poly1d([1,0,1])
deriv = np.polyder(secondFunc,1)
evalDeriv = np.polyval(deriv,1)
print(evalDeriv)


#%%

def newtonMeth(func, x,previous=0, count = 1):
    if count == 1: #very first x, there is nothing to compate it to 
        print(f"x{count} is {x:.3f}")
        newtonMeth(func, x, x, count+1) 
    else:
        valueOfCurrentX = (x) - (np.polyval(func,x)/np.polyval(np.polyder(func,1),x)) #calculates newtons method 
        if valueOfCurrentX == 0: #the value that you entered is the root protects it from cases where the user enters in the acutal value of the root 
            print(f"x{count} is {valueOfCurrentX:.3f}")
            print(f"The final value with stabilized thousandths places is: {valueOfCurrentX:.3f}")
            roots = np.roots(func)
            count = 1
            for i in roots:
                print(f"The {count} root is {i:.3f}")
                count = count +1
            return
        else: #not a root 
            difference = abs(valueOfCurrentX - previous) #difference (can only do this after the first x)
            print(f"x{count} is {valueOfCurrentX:.3f}")
            if difference > 0.0001:
                newtonMeth(func, valueOfCurrentX, valueOfCurrentX, count+1)  
            else:
                print(f"The final value with stabilized thousandths places is: {valueOfCurrentX:.3f}")
                roots = np.roots(func)
                count = 1
                for i in roots:
                    print(f"The {count} root is {i:.3f}") #prints out roots
                    count = count +1
                return
    
def promptUser(): #prompts user for a list of coeffs and returns it 
    num = int(input("What is the highest power of the polynomial? "))
    times = num
    polyList = []
    while times >= 0:
        coef = float(input(f"Enter the Coefficient of x^{times}: "))
        polyList.append(coef)
        times = times -1
    return polyList

func = promptUser()
x1 = float(input("Enter a x1 value: "))
newtonMeth(np.poly1d(func),x1)   
#newtonMeth(np.poly1d([1,-4,0,1]),0.5)    This case works 

