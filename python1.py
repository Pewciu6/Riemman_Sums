import matplotlib.pyplot as plt
import numpy as np

def Calc_Function(x):
    return x**2

def Riemann(x):

    Area = 0

    Riemann_arguments = np.linspace(Start, End, x+1)
    Riemann_values = [0] * (x+1)

    for i in range(1, len(Riemann_arguments)):
        Riemann_values[i] = Calc_Function((Riemann_arguments[i-1] + Riemann_arguments[i])/2)
        Area += Riemann_values[i]

    plt.title(f'Area: {Area}')
    plt.plot(Riemann_arguments, Riemann_values,'b.')
    plt.bar(Riemann_arguments, Riemann_values, (End-Start)/x)
    plt.plot(Arguments,Values, color="blue")
    plt.draw()

Start = int(input('Your sum starts at point a equal to: '))
End = int(input('Stops at point b equal to: '))
Partition = int(input('What is your desirable partition size: '))

Arguments = np.linspace(Start, End, 1000)
Values = [Calc_Function(x) for x in Arguments]

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

for i in range(1, Partition, 5):
    plt.clf()
    Riemann(i)
    plt.pause(3)