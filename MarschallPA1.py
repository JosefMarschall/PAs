# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 13:06:48 2024

@author: JPMarschall
"""

from random import choice


from tabulate import tabulate

import time

def oneDimension(numSteps):
    Origin = 0
    CurrentPosition = 0
    OriginCount = 0

    for i in range(100):

        
        CurrentPosition = 0
        
        for j in range(numSteps):
            sign = choice([-1,1])
            CurrentPosition = CurrentPosition + sign
            if CurrentPosition == Origin:
                OriginCount = OriginCount+1
                break
    return OriginCount

def twoDimension(numSteps):
    Origin = 0
    OriginCount = 0
    for i in range(100):
        
        CurrentXPosition = 0
        CurrentYPosition = 0
        
        
        for j in range(numSteps):
            sign = choice([-1,1])
            XY = choice(['x','y'])
            if XY == 'x':
                CurrentXPosition = CurrentXPosition + sign
            if XY == 'y':
                CurrentYPosition = CurrentYPosition + sign
            if CurrentXPosition == Origin and CurrentYPosition == Origin:
                OriginCount = OriginCount+1
                break
    return OriginCount

def threeDimension(numSteps):
    Origin = 0
    OriginCount = 0
    starttime=time.time()
    for i in range(100):
        CurrentXPosition = 0
        CurrentYPosition = 0
        CurrentZPosition = 0
        
        for j in range(numSteps):
            sign = choice([-1,1])
        
            
            XYZ = choice(['x','y','z'])
            if XYZ == 'x':
                CurrentXPosition = CurrentXPosition + sign
            if XYZ == 'y':
                CurrentYPosition = CurrentYPosition + sign
            if XYZ == 'z':
                CurrentZPosition = CurrentZPosition + sign
            if CurrentXPosition == Origin and CurrentYPosition == Origin and CurrentZPosition == Origin:
                OriginCount = OriginCount+1
                break

    time_for_loop=time.time() - starttime
    return OriginCount, time_for_loop


def printTable (numSteps1,numSteps2,numSteps3,numSteps4,numSteps5,numSteps6):
    # Sample data
    #I used this to save the two varibales returned by threeDimension() based on the number of steps 
    perc3D20, time3D20 = threeDimension(numSteps1)
    perc3D200, time3D200 = threeDimension(numSteps2)
    perc3D2000, time3D2000 = threeDimension(numSteps3)
    perc3D20000, time3D20000 = threeDimension(numSteps4)
    perc3D200000, time3D200000 = threeDimension(numSteps5)
    perc3D2000000, time3D2000000 = threeDimension(numSteps6)

    
    print("Percentage of times it reaches the origin:")
    data = [
        ["1D", oneDimension(numSteps1),oneDimension(numSteps2),oneDimension(numSteps3),oneDimension(numSteps4),oneDimension(numSteps5),oneDimension(numSteps6)],
        ["2D", twoDimension(numSteps1),twoDimension(numSteps2),twoDimension(numSteps3),twoDimension(numSteps4),twoDimension(numSteps5),twoDimension(numSteps6)],
        ["3D", perc3D20,perc3D200,perc3D2000,perc3D20000,perc3D200000,perc3D2000000]
    ]

    # Table headers
    headers = ["Number of Steps:", "20", "200", "2000", "20000", "200000", "2000000"]
    table = tabulate(data,headers,tablefmt = "grid")
    print(table)
    
    data = [
        ["3D", time3D20,time3D200,time3D2000,time3D20000,time3D200000,time3D2000000]
    ]

    # Table headers
    print("Runtime (in seconds):")
    headers = ["Number of Steps:", "20", "200", "2000", "20000", "200000", "2000000"]
               
    table = tabulate(data,headers,tablefmt = "grid")
    print(table)
    
def main():
    printTable(20,200,2000,20000,200000,2000000)


main()
    
    