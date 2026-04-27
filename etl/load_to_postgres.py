import pandas as pd
from sqlalchemy import create_engine

print("Alustan CSV failide laadimist...")

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5433/lasteaiakohad"
)

population_df = pd.read_csv("Outputs/rakvere_rahvastiku_prognoos_2026_2035.csv")
kinder_df = pd.read_csv("Outputs/rakvere_lasteaiavajadus_2026_2030.csv")
birth_df = pd.read_csv("Outputs/rakvere_synnid_2026_2035.csv")

print("CSV failid loetud.")
print("population rows:", len(population_df))
print("kinder rows:", len(kinder_df))
print("birth rows:", len(birth_df))

population_df.to_sql("population", engine, if_exists="replace", index=False)
kinder_df.to_sql("kinder", engine, if_exists="replace", index=False)
birth_df.to_sql("births", engine, if_exists="replace", index=False)

print("Andmed edukalt PostgreSQL-i laetud 🚀")
