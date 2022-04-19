import csv
import pandas

# with open("weather_data.csv") as data_file:
#     # creates csv reader object
#     data = csv.reader(data_file)
#     temperatures = []
#     # loop through each row
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# print("\nCSV files using Pandas:\n")
# data1 = pandas.read_csv("weather_data.csv")
# print(data1)
# print("These are the temperatures:\n")
# print(data1["temp"])
# print("Type check:\n", type(data1), type(data1["temp"]))
# # get average from data using Pandas
# print(data1["temp"].mean())
# # get maximum value from data using Pandas
# print("Max:", data1["temp"].max())

# print(data1.condition)
# # print row where temp is the maximum
# print(data1[data1.temp == data1.temp.max()])

# # creating a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data3 = pandas.DataFrame(data_dict)
# print(data3)
# data3.to_csv("./new_data.csv")

data_colour = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# we are looking for the colour "gray" within the column "primary fur color"
# print where condition is true
gray_squirrels_count = len(data_colour[data_colour["Primary Fur Color"] == "Gray"])
print(gray_squirrels_count)
# print black colour
black_squirrels_count = len(data_colour[data_colour["Primary Fur Color"] == "Black"])
print(black_squirrels_count)
# cinnamon colour
cin_squirrels_count = len(data_colour[data_colour["Primary Fur Color"] == "Cinnamon"])
print(cin_squirrels_count)

# create dictionary for dataframe
data_dictionary = {
    "Fur Colour": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, black_squirrels_count, cin_squirrels_count]
}

# create dataframe
data = pandas.DataFrame(data_dictionary)
print(data)
data.to_csv("./fur_colour_data.csv")