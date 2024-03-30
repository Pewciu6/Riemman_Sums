import matplotlib.pyplot as plt
import numpy as np
from Calculation_Function import *

def Right_Riemman_Sum(Temp_Number_Of_Partitions, Start, End, Arguments, Values):
    
    Calculated_Area = 0
    delta_X = (End-Start)/Temp_Number_Of_Partitions

    Riemman_arguments = np.linspace(Start, End, Temp_Number_Of_Partitions+1)
    Riemann_values = Calc_Function(Riemman_arguments)

    Riemman_arguments = Riemman_arguments[1:]
    Riemann_values = Riemann_values[1:]

    for x in Riemann_values:
        Calculated_Area += x*delta_X
    
    plt.title(f'Area: {Calculated_Area}')
    plt.plot(Riemman_arguments, Riemann_values,'b.', markersize=10)
    plt.bar(Riemman_arguments, Riemann_values, width=-(End-Start)/Temp_Number_Of_Partitions, align="edge", alpha=0.5,edgecolor='b')
    plt.plot(Arguments,Values, 'b')
    plt.draw()
