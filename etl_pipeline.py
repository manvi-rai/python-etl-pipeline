import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

df = pd.read_csv("data/employee.csv")

df["annual_salary"] = df["salary"] * 12
df = df[df["salary"] >= 0]

password = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql+psycopg2://postgres:{password}@localhost:5432/de_practice"
)

df.to_sql("employee_etl", engine, if_exists="replace", index=False)

print("Data loaded successfully")