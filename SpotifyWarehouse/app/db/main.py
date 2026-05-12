import psycopg
import flask

from setup import get_conn
from pathlib import Path
import pandas as pd
from matplotlib import pyplot as plt

# TODO
# 1. (ok) Connect psycopg with database
# 2. (ok) Test queries
# 3. (ok) Init the DB
# 4. Clean the data
#    - (ok) Null values -> None found
#    - (ok) Normalize some of them
#    - (ok) Min & max for ranges?
# 5. (nope) Repeating values -> covers
#    - (nope) Make unique -> add column ['Title + artist'] -> append ' by {Artist}' at the end
# 6. Insert data into intermediate table?
#    - Read about psycopg interaction with.csv
# 7. Insert into the DB

scripts = Path("scripts/")
datasets = Path("data/")

def exec_sql(location : str | Path):
    ''' Executes a specific query from .sql file. '''
    with open(location, "r") as f:
        schema = f.read()

    if schema:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(schema)

def init_schema():
    ''' Inits the DB. If tables don't exist, they are created. '''
    exec_sql(scripts / "dw-schema.sql")
    exec_sql(scripts / "data-staging-area.sql")

def load_data_to_staging_area(src : str | Path):
    ''' Loads data from the .csv into the staging area - full_dataset table. '''

    # 0. Read data from .csv

    df = pd.read_csv(src)

    # 1. Construct the SQL query

    cols_num = len(df.columns)
    query = "(" + "%s," * (cols_num - 1) + "%s)"
    query += 

    with get_conn() as conn:
        with conn.cursor() as cur:
            for idx, row in df.iterrows():
                cur.execute("INSERT INTO full_dataset "
                            "()"
                            "VALUES ()")

def explore_dataset():

    df = pd.read_csv(datasets / "spotify-dataset.csv")

    print(f"Column types: {df.dtypes}")
    print(f"Shape: {df.shape}")
    print(f"Title & views: {df.loc[[0, 5], ['Track', 'Views']]}")
    print(f"Title - Views: {df.loc[0: 5, 'Track': 'Views']}")
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

def clean_dataset(normalize=False):
    '''
    Removes null values from spotify-dataset.csv & rows which have not information about some youtube statistics.
    Normalization of some metrics is commented out.
    '''

    # 0. Read csv

    df = pd.read_csv(datasets / "spotify-dataset.csv")

    # 1. Null values removed

    # Null values: ['Channel'] & ['Title'] == 0
    not_on_yt = (df["Channel"] == '0') & (df["Title"] == '0')
    cleaned_df = df[~not_on_yt]

    # 2. Find min / max for each range column

    range_cols = ["Danceability", "Energy", "Loudness", "Speechiness", "Acousticness", "Instrumentalness", "Liveness", "Valence", "Tempo", "Duration_min", "Views", "Likes", "Comments", "Stream", "EnergyLiveness"]
    ranges_df = df.loc[ : , range_cols]
    maxes = ranges_df.max()
    mins = ranges_df.min()

    min_maxes = list(zip(mins, maxes))
    ranges = dict(zip(range_cols, min_maxes))

    # Save ranges into separate df

    ranges_df = pd.DataFrame(ranges)
    ranges_df.to_csv(datasets / "spotify-dataset-ranges.csv")

    if normalize:
        # 3. Normalize the cleaned df
        clean_norm_df = (ranges_df - ranges_df.min()) / (ranges_df.max() - ranges_df.min())

        # 4. Replace cols in cleaned df with normalized ones
        for col in clean_norm_df.columns:
            new_col = col + "-norm"
            cleaned_df[new_col] = clean_norm_df[col]

    # 5. Save to 'spotify-dataset-clean.csv'
    cleaned_df.to_csv(datasets / "spotify-dataset-clean.csv")

def dataset_messing():
    df = pd.read_csv(datasets / "spotify-dataset-clean.csv")

    _, row = next(df.iterrows())
    cols = [col.lower() for col in tuple(row.index)]
    vals = row.values
    print(cols)
    print(vals)

# dataset_messing()
clean_dataset()


