import pandas as pd

# df = pd.read_csv("spectrum.csv")
# df = pd.read_csv("spectrum.csv", sep=r"\s+")
# print(df)

df2 = pd.read_csv("spectrum_no_header.csv", sep=r"\s+")
print(df2)
df2.info()

df3 = pd.read_csv("spectrum_no_header.csv", sep=r"\s+", header=None)
print(df3)

df4 = pd.read_csv("spectrum_no_header.csv", sep=r"\s+", header=None, names=["wavenumber",
"intensity"])
print(df4)

df5 = pd.read_csv("spectrum_no_header.csv", sep=r"\s+", header=None, names=["Wellenzahl",
"Intensität"])
print(df5)

df6 = pd.read_csv("spectrum_no_header_three_columns.csv", sep=r"\s+", usecols=[0,1], header=None, names=["Wellenzahl",
"Intensität"])
print(df6)