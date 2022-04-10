import csv

with open("weather_data.csv") as data_file:
    # creates csv reader object
    data = csv.reader(data_file)
    # loop through each row
    for row in data:
        print(row)
