# with open(r"C:\Upendra\Python\Python_Graphics\Weather\weather_data.csv") as weather_file:
#     daily_weather = weather_file.readlines()
#     print(daily_weather)


# import csv

# with open(r"C:\Upendra\Python\Python_Graphics\Weather\weather_data.csv") as weather_file:
#     weather_data = csv.reader(weather_file)
#     temperatures=[]
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(row[1])

#     print(temperatures)

import pandas

data = pandas.read_csv(r"C:\Upendra\Python\Python_Graphics\Weather\weather_data.csv")
temp_list=data["temp"].to_list()
max_temp=data["temp"].max()
# print(max_temp)

mon_temp=data[data.day == "Monday"].temp
mon_temp += 273
# print(mon_temp)

data_dict = {
    "names": ["s1","s2","s3"],
    "marks": [12,23,34]
}

data = pandas.DataFrame(data_dict)
data.to_csv("newfile.csv")