import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import scipy.constants as const
import matplotlib.pyplot as plt

df1 = pd.read_csv("exp_decay.csv")

def Y(t, tau,  a, b):
    return a * np.exp(-t / tau) + b

x = df1["time_min"].values
y = df1["counts_per_min"].values

popt, pcov = curve_fit(Y, x, y, [25, 800, 30])
tau, a, b = popt

halflife = tau * np.log(2)
print("halflife: ", halflife)
print("tau: ", tau)
print("a: ", a)
print("b: ", b)


# plt.plot(x,Y(x,tau,a,b), color="red")
# plt.plot(x,y, color="blue")
# plt.show()

perr = np.sqrt(np.diag(pcov))
dtau, da, db = perr

print("error tau: ", dtau)
print("error a: ", da)
print("error b: ", db)

residuum = (y - Y(x, tau, a, b) )/np.sqrt(Y(x, tau, a, b))

print(np.std(y))

# print(residuen)

# plt.scatter(x,residuen, s=3)
plt.hist(residuum, bins=20, color='blue', edgecolor='black', range = (-5,5))
plt.show()