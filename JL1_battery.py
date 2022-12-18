import csv
import time
import numpy as np
import datetime

# Import the Joulescope API module
import joulescope

# Scan for and connect to Joulescope
with joulescope.scan_require_one(config='auto') as js:
    # Set up the CSV file for writing
    csv_file = open('JL1B.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file)

    # Write the header row to the CSV file
    csv_writer.writerow(['Time', 'Voltage', 'Current'])

    # Initialize the counter variable
    count = 0

    # Gather data for 130 seconds
    start_time = time.time()
    while time.time() - start_time < 100:
        # Get the current voltage and current data from Joulescopes
        data = js.read(contiguous_duration=1)
        current, voltage = np.mean(data, axis=0)

        # Print the data to the command prompt
        print(f"Count: {count}, Voltage: {voltage}, Current: {current}")

        # Convert the outputted time to military time format
        time_military = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')

        # Write the data to the CSV file
        csv_writer.writerow([time_military, voltage, current])

        # Increment the counter variable
        count += 1

    # Close the CSV file
    csv_file.close()

# Disconnect from Joulescope
js.disconnect()