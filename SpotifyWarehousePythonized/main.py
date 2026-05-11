import psycopg
import flask

from setup import get_cursor, get_conn
from pathlib import Path
import pandas as pd
from matplotlib import pyplot as plt


# TODO
# 1. (ok) Connect psycopg with database
# 2. (ok) Test queries
# 3. (ok) Init the DB
# 4. Clean the data
#    - Null values
#    - Normalize some of them
#    - Min & max for ranges?
# 5. Insert data into intermediate table?
# 6. Insert into the DB

scripts = Path("scripts/")
datasets = Path("data/")

def exec_sql(location : str | Path):
    with open(location, "r") as f:
        schema = f.read()

    if schema:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(schema)

def init_schema():
    exec_sql(scripts / "dw-schema.sql")
    exec_sql(scripts / "data-staging-area.sql")

def clean_dataset():
    # 0. Read csv

    df = pd.read_csv(datasets / "spotify-dataset.csv")

    # 0.1 Explore df

    print(f"Column types: {df.dtypes}")
    print(f"Shape: {df.shape}")
    print(f"Title & views: {df.loc[[0, 5], ['Track', 'Views']]}")
    print(f"Title - Views: {df.loc[0 : 5, 'Track' : 'Views']}")
    print(f"[5, 1]: {df.iloc[5, 1]}")
    print(f"Index: {df.index}")
    print(f"Columns: {df.columns}")
    print(f"Nulls: {df.isnull()}")
    print(f"Any nulls: {df[df.isnull()]}")
    print(f"Any artist null: {df['Artist'].isnull()}")
    print(f"Artist that is null: {df[df['Artist'].isnull()].index}")
    print(f"Views description: {df['Views'].describe()}")
    print(f"Artist counts: {df['Artist'].value_counts()}")

    print("All counts")

    # All counts:
    for col in df.columns:
        print(f"{col} :")
        print(f"{df[col].value_counts()}")

    print(f"Null titles: {}")

    print("Histograms: ")

   # for col in df.columns:
        #pd.Series(list(df[col])).plot.hist()
        #plt.show()


    # 1. Null values removed

    # 2. Find min / max for each column

clean_dataset()



