#!/usr/bin/python

#The following statements are used to import numpy and matplotlib.
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate2

x = np.arange(0,np.pi, 0.01)
y = np.sin(x)
plt.plot(x,y)
plt.show()


b = np.cos(x)
plt.plot(x,b)
plt.show()

# TODO fill in this function
def integrate(y, dx):
    tempY = np.array(y) * dx
    integral = 0.0
    for values in tempY:
        integral += values
    return integral

print(integrate(y, 0.01))
print(integrate2.quad((lambda x: np.sin(x)), 0, np.pi))
print(integrate(b, 0.01))
print(integrate2.quad((lambda x: np.cos(x)), 0, np.pi))


# TODO write code here to setup arrays x and y = sin(x) and then plot them.
# After this is done implement your integrate function above integrate y
