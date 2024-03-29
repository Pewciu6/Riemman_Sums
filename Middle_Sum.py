import matplotlib.pyplot as plt
import numpy as np
from Calculation_Function import *

def Middle_Sum_Riemann(Number_Of_Partitions, Start, End, Arguments, Values):

    Calculated_Area = 0

    Riemman_arguments = np.linspace(Start, End, Number_Of_Partitions+1)
    Riemann_values = [0] * (Number_Of_Partitions+1)

    for i in range(1, len(Riemman_arguments)):
        Riemann_values[i] = Calc_Function((Riemman_arguments[i-1] + Riemman_arguments[i])/2)
        Calculated_Area += Riemann_values[i]

    plt.title(f'Area: {Calculated_Area}')
    plt.plot(Riemman_arguments, Riemann_values,'b.')
    plt.bar(Riemman_arguments, Riemann_values, (End-Start)/Number_Of_Partitions)
    plt.plot(Arguments,Values, color="blue")
    plt.draw()