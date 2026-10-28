import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
engine=create_engine(
    "postgresql://postgres:root@localhost:5432/taxi_data_platform"
)
#daily bases
daily_df=pd.read_sql(
    "select * from daily_summary",
    engine
)
print(daily_df.head())
#hourly bases
hourly_df=pd.read_sql(
    "select * from hourly_summary",
    engine
)
#location bases
location_df=pd.read_sql(
    "select * from location_summary",
    engine
)
plt.figure()

plt.plot(
    daily_df["pickup_date"],
    daily_df["total_revenue"]
)

plt.xlabel("Date")
plt.ylabel("Total Revenue")
plt.title("Daily Taxi Revenue")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()

plt.plot(
    hourly_df["pickup_hour"],
    hourly_df["total_trips"]
)

plt.xlabel("Pickup Hour")
plt.ylabel("Total Trips")
plt.title("Taxi Trips by Hour")

plt.xticks(range(24))
plt.tight_layout()
plt.show()

top_locations = (
    location_df
    .groupby("pickup_zone")
    ["total_revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure()

top_locations.plot(kind="bar")

plt.xlabel("Pickup Zone")
plt.ylabel("Total Revenue")
plt.title("Top 10 Pickup Zones by Revenue")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()