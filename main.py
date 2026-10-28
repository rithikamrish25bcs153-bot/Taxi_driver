import pandas as pd
import glob
import validation

DATA_FOLDER="data/raw/"
ERROR_FOLDER="data/errors/"
PROCESSED_FOLDER="data/processed/"

PROJECT_COLUMNS=[
    "VendorID",
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime",
    "passenger_count",
    "trip_distance",
    "RatecodeID",
    "PULocationID",
    "DOLocationID",
    "payment_type",
    "fare_amount",
    "tip_amount",
    "tolls_amount",
    "total_amount",
    "congestion_surcharge"
]
#loading/ extraction
def load_data(file_path):
    return pd.read_parquet(file_path)

def create_project_data(df,columns):
    return df[columns].copy()
#transforming
def validate_data(df, month):
    df = validation.check_vendor_id(df)
    df = validation.check_pickup_datetime(df, month)
    df = validation.check_dropoff_datetime(df, month)
    df = validation.check_passenger_count(df)
    df = validation.check_trip_distance(df)
    df = validation.check_ratecode_id(df)
    df = validation.check_pu_location_id(df)
    df = validation.check_do_location_id(df)
    df = validation.check_payment_type(df)
    df = validation.check_fare_amount(df)
    df = validation.check_tip_amount(df)
    df = validation.check_tolls_amount(df)
    df = validation.check_total_amount(df)
    df = validation.check_congestion_surcharge(df)

    return df

def main():
    print("Start taxi data pipeline...")
    files=glob.glob(DATA_FOLDER+"*.parquet") 

    for file in files:
        print(f"Processing: {file}")
        file_name=file.split("\\")[-1]
        month=file_name.replace("yellow_tripdata_","").replace(".parquet","")
        print(f"Expected month: {month}")

        df=load_data(file)
        print(f"Raw record:{len(df)}")

        project_df=create_project_data(df,PROJECT_COLUMNS)
        project_df["invalid"] = ""

        project_df = validate_data(project_df, month)

        invalid_records = project_df[project_df["invalid"] != ""]

        valid_records = project_df[project_df["invalid"] == ""]
        if not invalid_records.empty:
            error_file = ERROR_FOLDER + file.split("\\")[-1].replace(
                ".parquet",
                "_errors.csv"
            )
            invalid_records.to_csv(error_file, index=False)
            print(f"Invalid records found: {len(invalid_records)}")
        else:
            print("No invalid records found")
        valid_records=valid_records[PROJECT_COLUMNST]
        processed_file = PROCESSED_FOLDER + file_name.replace(
            ".parquet",
            "_processed.parquet"
        )
        valid_records.to_parquet(processed_file, index=False)
        print(f"Processed records saved: {len(valid_records)}")
if __name__=="__main__":
    main()