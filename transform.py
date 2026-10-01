import pandas as pd

df= pd.read_csv("data/employee.csv")

df["annual_salary"] = df ["salary"] * 12
df= df[ df["salary"] >=0]
print(df)
