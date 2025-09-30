import numpy as np
import matplotlib.pyplot as plt
import math


def derive(f,h, x):
    deriv = []
    run = x[0]
    while run < x[1]:
        d_x = (f(run+h) - f(run-h)) / (2*h) 
        deriv.append(d_x)
        run += h
    return deriv

def f(x): return np.sin(x)
# step = 0.005
intervall =  [0, 10*np.pi]

def error(step):
    sin = derive(f, step, intervall)
    cos = []
    run = 0
    while run < intervall[1]:
        cos.append(np.cos(run))
        run += step

    npsin = np.array(sin)
    npcos = np.array(cos)

    error = np.abs(npsin - npcos)
    return error

max_error = []
for i in range (1, 50000):
    max_error.append(np.max(error(i/10000))) 

width = np.arange(1, 50000) * (1/10000)
plt.plot(width, max_error, color="red")
plt.xlabel(r"h")
plt.ylabel("Error")
plt.title(r"Error")
plt.xlim((0,5))
plt.legend(loc="upper left")
plt.show()