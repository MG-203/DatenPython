from scipy.interpolate import UnivariateSpline
import pandas as pd
import numpy as np

df = pd.read_csv("Barometer.csv")
t = df["seconds_elapsed"]
h = df["relativeAltitude"]

cubic_spline = UnivariateSpline(t, h, )