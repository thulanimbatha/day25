import csv
import pandas

with open("weather_data.csv") as data_file:
    # creates csv reader object
    data = csv.reader(data_file)
    temperatures = []
    # loop through each row
    for row in data:
        print(row)
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
    
print("\nCSV files using Pandas:\n")
data1 = pandas.read_csv("weather_data.csv")
print(data1)
print("These are the temperatures:\n")
print(data1["temp"])