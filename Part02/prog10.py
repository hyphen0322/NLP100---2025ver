import pandas as pd

df = pd.read_table("popular-name.txt", sep="\t", header=None)
print(len(df))