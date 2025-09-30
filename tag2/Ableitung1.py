import numpy as np
from scipy.optimize import approx_fprime


f = lambda x: np.sin(x[0]) * np.cos(x[1])

x_0 = np.array([np.pi/4, np.pi/3])

grad = approx_fprime(x_0, f)
print(grad)

exact_grad = lambda x: [np.cos(x[0])*np.cos(x[1]), -np.sin(x[0]*np.sin(x[1]))]
print(exact_grad(x_0))