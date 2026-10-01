import os
import logging

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()

logging.info("ETL started")

df = pd.read_csv("data/employee.csv")
logging.info("Data extracted successfully")

df["annual_salary"] = df["salary"] * 12

df = df[df["salary"] >= 0]

password = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql+psycopg2://postgres:{password}@localhost:5432/de_practice"
)

df.to_sql("employee_etl", engine, if_exists="replace", index=False)

logging.info("Data loaded successfully")