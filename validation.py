import pandas as pd


def check_vendor_id(df):
    missing = df["VendorID"].isnull()
    print("Missing VendorID:", missing.sum())
    df.loc[missing, "invalid"] = "Missing VendorID"

    return df


def check_pickup_datetime(df, month):
    missing = df["tpep_pickup_datetime"].isnull()
    print("Missing Pickup Datetime:", missing.sum())
    df.loc[missing, "invalid"] = "Missing Pickup Datetime"

    pickup = pd.to_datetime(
        df["tpep_pickup_datetime"],
        errors="coerce"
    )

    pickup_month = pickup.dt.strftime("%Y-%m")
    wrong_month = pickup_month != month

    print("Wrong Pickup Month:", wrong_month.sum())
    df.loc[wrong_month, "invalid"] = "Wrong Pickup Month"

    return df


def check_dropoff_datetime(df, month):
    missing = df["tpep_dropoff_datetime"].isnull()
    print("Missing Dropoff Datetime:", missing.sum())
    df.loc[missing, "invalid"] = "Missing Dropoff Datetime"

    dropoff = pd.to_datetime(
        df["tpep_dropoff_datetime"],
        errors="coerce"
    )

    dropoff_month = dropoff.dt.strftime("%Y-%m")
    wrong_month = dropoff_month != month

    print("Wrong Dropoff Month:", wrong_month.sum())
    df.loc[wrong_month, "invalid"] = "Wrong Dropoff Month"

    return df


def check_passenger_count(df):
    missing = df["passenger_count"].isnull()
    print("Missing Passenger Count:", missing.sum())
    df.loc[missing, "invalid"] = "Missing Passenger Count"

    invalid_count = df["passenger_count"] <= 0
    print("Invalid Passenger Count:", invalid_count.sum())
    df.loc[invalid_count, "invalid"] = "Invalid Passenger Count"

    return df


def check_trip_distance(df):
    missing = df["trip_distance"].isnull()
    print("Missing Trip Distance:", missing.sum())
    df.loc[missing, "invalid"] = "Missing Trip Distance"

    invalid_distance = df["trip_distance"] <= 0
    print("Invalid Trip Distance:", invalid_distance.sum())
    df.loc[invalid_distance, "invalid"] = "Invalid Trip Distance"

    return df


def check_ratecode_id(df):
    missing = df["RatecodeID"].isnull()
    print("Missing RatecodeID:", missing.sum())
    df.loc[missing, "invalid"] = "Missing RatecodeID"

    invalid_ratecode = ~df["RatecodeID"].isin([1, 2, 3, 4, 5, 6, 99])
    print("Invalid RatecodeID:", invalid_ratecode.sum())
    df.loc[invalid_ratecode, "invalid"] = "Invalid RatecodeID"

    return df


def check_pu_location_id(df):
    missing = df["PULocationID"].isnull()
    print("Missing PULocationID:", missing.sum())
    df.loc[missing, "invalid"] = "Missing PULocationID"

    invalid_location = df["PULocationID"] <= 0
    print("Invalid PULocationID:", invalid_location.sum())
    df.loc[invalid_location, "invalid"] = "Invalid PULocationID"

    return df


def check_do_location_id(df):
    missing = df["DOLocationID"].isnull()
    print("Missing DOLocationID:", missing.sum())
    df.loc[missing, "invalid"] = "Missing DOLocationID"

    invalid_location = df["DOLocationID"] <= 0
    print("Invalid DOLocationID:", invalid_location.sum())
    df.loc[invalid_location, "invalid"] = "Invalid DOLocationID"

    return df


def check_payment_type(df):
    missing = df["payment_type"].isnull()
    print("Missing Payment Type:", missing.sum())
    df.loc[missing, "invalid"] = "Missing Payment Type"

    invalid_payment = ~df["payment_type"].isin([0, 1, 2, 3, 4, 5, 6])
    print("Invalid Payment Type:", invalid_payment.sum())
    df.loc[invalid_payment, "invalid"] = "Invalid Payment Type"

    return df


def check_fare_amount(df):
    missing = df["fare_amount"].isnull()
    print("Missing Fare Amount:", missing.sum())
    df.loc[missing, "invalid"] = "Missing Fare Amount"

    invalid_fare = df["fare_amount"] < 0
    print("Invalid Fare Amount:", invalid_fare.sum())
    df.loc[invalid_fare, "invalid"] = "Invalid Fare Amount"

    return df


def check_tip_amount(df):
    missing = df["tip_amount"].isnull()
    print("Missing Tip Amount:", missing.sum())
    df.loc[missing, "invalid"] = "Missing Tip Amount"

    invalid_tip = df["tip_amount"] < 0
    print("Invalid Tip Amount:", invalid_tip.sum())
    df.loc[invalid_tip, "invalid"] = "Invalid Tip Amount"

    return df


def check_tolls_amount(df):
    missing = df["tolls_amount"].isnull()
    print("Missing Tolls Amount:", missing.sum())
    df.loc[missing, "invalid"] = "Missing Tolls Amount"

    invalid_tolls = df["tolls_amount"] < 0
    print("Invalid Tolls Amount:", invalid_tolls.sum())
    df.loc[invalid_tolls, "invalid"] = "Invalid Tolls Amount"

    return df


def check_total_amount(df):
    missing = df["total_amount"].isnull()
    print("Missing Total Amount:", missing.sum())
    df.loc[missing, "invalid"] = "Missing Total Amount"

    invalid_total = df["total_amount"] < 0
    print("Invalid Total Amount:", invalid_total.sum())
    df.loc[invalid_total, "invalid"] = "Invalid Total Amount"

    return df


def check_congestion_surcharge(df):
    missing = df["congestion_surcharge"].isnull()
    print("Missing Congestion Surcharge:", missing.sum())
    df.loc[missing, "invalid"] = "Missing Congestion Surcharge"

    invalid_surcharge = df["congestion_surcharge"] < 0
    print("Invalid Congestion Surcharge:", invalid_surcharge.sum())
    df.loc[invalid_surcharge, "invalid"] = "Invalid Congestion Surcharge"

    return df