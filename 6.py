import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("spectrum_no_header.csv", sep=r"\s+", header=None ,names=["Wellenzahl",
"Intensität"])
print(df)
df.info()

#21)
# print(df.iloc[15,1])
#22)
# print(df.iloc[50:61])
#23)
# print(df.loc[0:2000, "Intensität"])

#24)
# print(df.iloc[:,1])
# print(df.loc[:,"Intensität"])
# print(df["Wellenzahl"])


# print(df.loc[df["Wellenzahl"] <= 2000.0])

#26)
df_slice = df.loc[(df["Wellenzahl"] >= 1000) & (df["Wellenzahl"] <= 2000)]
plt.plot(df_slice["Wellenzahl"], df_slice["Intensität"], color="green", label="Spektrum 1")
plt.xlabel(r"Wellenzahl / cm$^{-1}$")
plt.ylabel("Intensität / a.u.")
plt.title(r"Schwingungsspektrum von C$_{120}^-$")
plt.xlim((1000,2000))
plt.legend(loc="upper left")
plt.show()