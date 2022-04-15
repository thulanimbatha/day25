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
print("Type check:\n", type(data1), type(data1["temp"]))
# get average from data using Pandas
print(data1["temp"].mean())
# get maximum value from data using Pandas
print("Max:", data1["temp"].max())

print(data1.condition)
# print row where temp is the maximum
print(data1[data1.temp == data1.temp.max()])

# creating a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data3 = pandas.DataFrame(data_dict)
print(data3)
data3.to_csv("./new_data.csv")
