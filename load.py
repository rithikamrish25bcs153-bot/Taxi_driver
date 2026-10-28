import pandas as pd
import glob
files=glob.glob("data/transformed/*.parquet")

for file in files:
    df=pd.read_parquet(file)
    print(df.head())
    print(df.shape)

from sqlalchemy import create_engine
engine=create_engine('postgresql://postgres:root@localhost:5432/taxi_data_platform')
try:
    with engine.connect() as connection:
        print("PostgreSql connection successfully")
except Exception as e:
    print("PostgreSql connection failed",e)

daily_df=pd.read_parquet(
    "data/transformed/daily_summary.parquet"
)
daily_df.to_sql(
    "daily_summary",
    engine,
    if_exists="replace",
    index=False,
)
print("Daily_summary loaded successfully")
hourly_df=pd.read_parquet(
    "data/transformed/hourly_summary.parquet"
)
hourly_df.to_sql(
    "hourly_summary",
    engine,
    if_exists="replace",
    index=False,
)
print("Hourly_summary loaded successfully")
location_df=pd.read_parquet(
    "data/transformed/location_summary.parquet"
)
location_df.to_sql(
        "location_summary",
        engine,
        if_exists="replace",
        index=False,
)
print("Location_Summary loaded successfully")