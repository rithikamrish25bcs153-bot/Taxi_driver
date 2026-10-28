import pandas as pd
import glob
import os

PROCESSED_FOLDER = "data/processed/"
ZONE_FILE = "data/taxi_zone_lookup.csv"
TRANSFORMED_FOLDER="data/transformed/"

os.makedirs(TRANSFORMED_FOLDER, exist_ok=True)# is it doest

hourly_summaries=[]
daily_summaries=[]
location_summaries=[]

zone_df = pd.read_csv(ZONE_FILE)

# Pickup lookup
pickup_zone = zone_df.rename(
    columns={
        "LocationID": "PULocationID",
        "Borough": "pickup_borough",
        "Zone": "pickup_zone",
        "service_zone": "pickup_service_zone"
    }
)
# Dropoff lookup
dropoff_zone = zone_df.rename(
    columns={
        "LocationID": "DOLocationID",
        "Borough": "dropoff_borough",
        "Zone": "dropoff_zone",
        "service_zone": "dropoff_service_zone"
    }
)
files = glob.glob(PROCESSED_FOLDER + "*.parquet")

for file in files:
    print("Processing:", file)
    file_name=file.split("\\")[-1]
    month=file_name.replace(
        "yellow_tripdata_",""
    ).replace(
        "_processed.parquet",""
    )

    df = pd.read_parquet(file)
    df["month"]=month
# TIME
    df["pickup_date"]=df["tpep_pickup_datetime"].dt.date
    df["pickup_hour"]=df["tpep_pickup_datetime"].dt.hour
    df["day_of_week"]=df["tpep_pickup_datetime"].dt.day_name()

# TRIP
    df["trip_duration_minutes"] = (
        df["tpep_dropoff_datetime"]
        - df["tpep_pickup_datetime"]
    ).dt.total_seconds() / 60

# REVENUE
    df["revenue_per_passenger"]=(
        df["total_amount"] / df["passenger_count"]
    )

    df["tip_percentage"]=(
        df["tip_amount"]/df["fare_amount"]
    ) * 100

    df = df.merge(
        pickup_zone,
        on="PULocationID",
        how="left"
    )

    df = df.merge(
        dropoff_zone,
        on="DOLocationID",
        how="left"
    )

    location_summary=(
        df.groupby(["month","PULocationID", "pickup_borough", "pickup_zone"])
        .agg(
            total_trip=("PULocationID", "count"),
            total_revenue=("total_amount", "sum"),
        )
        .reset_index()
    )
    location_summaries.append(location_summary)

    hourly_summary = (
        df.groupby(["month","pickup_hour"])
        .agg(
            total_trips=("pickup_hour", "count"),
            total_revenue=("total_amount", "sum")
        )
        .reset_index()
    )

    hourly_summaries.append(hourly_summary)

    daily_summary=(
        df.groupby("pickup_date")
        .agg(
            total_trips=("pickup_date", "count"),
            total_revenue=("total_amount", "sum"),
        )
        .reset_index()
    )
    daily_summaries.append(daily_summary)
all_hours_summary=pd.concat(
    hourly_summaries,
    ignore_index=True
)
all_daily_summary=pd.concat(
    daily_summaries,
    ignore_index=True
)
all_location_summary=pd.concat(
    location_summaries,
    ignore_index=True
)
all_hours_summary.to_parquet(
    TRANSFORMED_FOLDER+"hourly_summary.parquet",
    index=False
)
all_daily_summary.to_parquet(
    TRANSFORMED_FOLDER+"daily_summary.parquet",
    index=False
)
all_location_summary.to_parquet(
    TRANSFORMED_FOLDER+"location_summary.parquet",
    index=False
)