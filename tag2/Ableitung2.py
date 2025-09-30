import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv("Barometer.csv", sep=r",", usecols=[0,1])
# print(df1)
# plt.plot(df1["seconds_elapsed"], df1["relativeAltitude"], color="red")
# plt.xlabel(r"Sekunden")
# plt.ylabel("Höhe in m")
# plt.title(r"Höhenverlauf")
# plt.xlim((0,100))
# plt.legend(loc="upper left")

verticle_velocity = np.gradient(df1["relativeAltitude"], df1["seconds_elapsed"])
print(verticle_velocity)

max_velocity = np.max(verticle_velocity)
min_velocity = np.min(verticle_velocity)
print("maximal velocity: ", max_velocity)
print("minimal velocity: ", min_velocity)

fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True)
axs[0].plot(df1["seconds_elapsed"], df1["relativeAltitude"], color="red", label="Altitude")
axs[1].plot(df1["seconds_elapsed"], verticle_velocity, color="blue", label="verticle velocity")
axs[1].set_xlabel(r"Seconds")
axs[0].set_ylabel("relativeAltitude")
axs[1].set_ylabel("Verticle Velocity")
axs[1].set_xlim((np.min(df1["seconds_elapsed"]),np.max(df1["seconds_elapsed"])))
axs[0].legend()
axs[1].legend()
plt.show()