import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = "US_Accidents_Dec21_updated.csv"

# Turn file into pandas dataframe
df = pd.read_csv(data)
# print(df.head)

# Get the names of columns for removing to make smaller CSV file
for col in df.columns:
    print(col)

# Show which columns are missing the most data
print(df.isnull().sum() / len(df))

# Drop columns
df = df.drop(columns=["Number", "Street", "City", "Zipcode", "Timezone", "Airport_Code", "Wind_Direction",
                      "Wind_Speed(mph)", "Precipitation(in)", "Weather_Condition", "Amenity", "Amenity",
                      "Bump", "Crossing", "Give_Way", "Junction", "No_Exit", "Railway", "Roundabout",
                      "Station", "Stop", "Traffic_Calming", "Traffic_Signal", "Turning_Loop", "Wind_Chill(F)",
                      "Humidity(%)", "Pressure(in)", "Astronomical_Twilight", "Nautical_Twilight", "Civil_Twilight"])

# Remove any outliers in temp
q_low = df["Temperature(F)"].quantile(0.01)
q_hi = df["Temperature(F)"].quantile(0.99)
df = df[(df["Temperature(F)"] < q_hi) & (df["Temperature(F)"] > q_low)]

# Send cleaned dataframe to new CSV
df.to_csv("US_Accidents_Cleaned.csv", index=False)




