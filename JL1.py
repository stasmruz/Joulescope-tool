# Import dependencies
import pandas as pd
import numpy as np

# Import the csv file
df1 = pd.read_csv("JL1B.csv")

# Calculate the mean voltage and current values
bvoltage = df1['Voltage'].mean()
bcurrent = df1['Current'].mean()

# Print the results
print("JL1_battery")
print("Current:", bcurrent.round(4))
print("Voltage:", bvoltage.round(4))