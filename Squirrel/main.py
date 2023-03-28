import pandas as pd

data_file = pd.read_csv(r"C:\Upendra\Python\Python_Graphics\Squirrel\Squirrel_Data.csv")

gray_squirrel_count = len(data_file[data_file["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data_file[data_file["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data_file[data_file["Primary Fur Color"] == "Black"])
# print(gray_squirrel_count)
# print(red_squirrel_count)
# print(black_squirrel_count)

data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Squirrel Count":[gray_squirrel_count,red_squirrel_count,black_squirrel_count]
}

dataframe = pd.DataFrame(data_dict)
dataframe.to_csv("count_squirrel.csv")