""" import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []    
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))        
    print(temperatures) """
""" 
import pandas as pd
data = pd.read_csv("weather_data.csv")
print(type(data)) 
#  print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# avg = int(sum(temp_list) / len(temp_list))
print(f"the average temp is:", {data["temp"].mean()} )
print(data["temp"].max())

#Get data in columns
print(data.condition)
 
#Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_far = monday.temp * 9/5 + 32

print(monday_far)


#Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
"""
import pandas as pd

data = pd.read_csv("squirrel_data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

squirrelounts = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pd.DataFrame(squirrelounts)
df.to_csv("squirrel_count.csv")