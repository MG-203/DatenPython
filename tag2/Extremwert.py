import numpy as np
from scipy.optimize import minimize_scalar
import scipy.constants as const

v0 = 40

def R(theta):
    return -v0**2 / const.g * np.sin(2*theta)

theta_star = minimize_scalar(R)
print(theta_star)
