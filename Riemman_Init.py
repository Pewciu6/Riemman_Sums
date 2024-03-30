import matplotlib.pyplot as plt
import numpy as np
from Calculation_Function import *
from Left_Sum import Left_Riemman_Sum
from Right_Sum import Right_Riemman_Sum
from Middle_Sum import Middle_Sum_Riemann



while(True):
    
    Initialize = input("Would you like to calculate middle, left or perhaps right Riemman Sums?: ")

    if Initialize.lower() in ["middle","left","right"]:
        
        Start = int(input('Your sum starts at point a equal to: '))
        End = int(input('Stops at point b equal to: '))
        Partition = int(input('What is your desirable partition size: '))

        Arguments = np.linspace(Start, End, 1000)
        Values = [Calc_Function(x) for x in Arguments]

        plt.plot(Arguments, Values, color="red")
        plt.draw()

        if Initialize.lower() == "middle":
            
            for i in range(1, Partition+1, 3):
                plt.clf()
                Middle_Sum_Riemann(i, Start, End, Arguments, Values)
                plt.pause(2)

        elif Initialize.lower() == "right":

            for i in range(1, Partition+1, 3):
                plt.clf()
                Right_Riemman_Sum(i, Start, End, Arguments, Values)
                plt.pause(2)

        else:

            for i in range(1, Partition+1, 3):
                plt.clf()
                Left_Riemman_Sum(i, Start, End, Arguments, Values)
                plt.pause(2)

        plt.xlabel('X-Axis')
        plt.ylabel('Y-Axis')

    else:
        print(f'\nI am sorry, but it does not match any type of Riemman Sums, try again')