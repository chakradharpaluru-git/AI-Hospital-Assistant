import pandas as pd

df = pd.read_csv("datasets/disease_dataset.csv")
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

rows = df[df["high_fever"] == 1]

print("Diseases having high_fever:\n")
print(rows["prognosis"].value_counts())