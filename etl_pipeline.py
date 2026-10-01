import pandas as pd
import psycopg2
from sqlalchemy import create_engine

df = pd.read_csv("data/employee.csv")

df["annual_salary"] = df["salary"] * 12
df = df[df["salary"] >= 0]

engine = create_engine(
    "postgresql+psycopg2://postgres:manvirai25@localhost:5432/de_practice"
)

df.to_sql("employee_etl", engine, if_exists="append", index=False)

print("Data loaded successfully")