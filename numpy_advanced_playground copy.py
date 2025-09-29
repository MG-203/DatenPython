import numpy as np
import pandas as pd
df = pd.read_csv("spectrum_no_header.csv", sep=r"\s+", header=None, 
                 names=["Wellenzahl", "Intensität"])
# print(df)
# print(df.info())

array = np.array(df)
# print(array[:10, :])
# print(array[10:21,:])
print(array[array[:,1] > 1e-20,:])