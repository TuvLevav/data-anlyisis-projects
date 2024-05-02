import pandas
#loding csv using api and request modul
#looding csv file
data = pandas.read_csv("Social_Network_Ads.csv")
data_try = pandas.read_csv("Social_Network_Ads.csv")
data_ = pandas.read_csv("Social_Network_Ads.csv")
data_row = pandas.read_csv("Social_Network_Ads.csv")
data_add = pandas.read_csv("Social_Network_Ads.csv")

#acsess to colum
#1 ver
#data["colunm_label"]
gender_col = data["Gender"]
#2 ver
#data.colounm_label
gender = data.Gender
print(gender)
#acsess to row
#group of rows, sfisify by a common value
gender_row = data[data.Gender == "Male"]
#a spsific row, sfisify by a unic value
age_data = data.Age
lower_ages = data[age_data <= 30]
#we can do it with all of the  if stetment and get this row data, we can sfisify colunm into it

#add row or col
new_row = data[data.Age <= 30]
data_add = data_add._append(new_row)
#this is not work
"""data_add.loc['new_row'] = data[data.Age == 19]
print(data_add.tail())"""
#how to add a row to sfisific place
#remove col
#one at once
del data_try['Age']
#
data_try=data_try.drop(["Gender","Purchased"], axis=1)
#remove by index
data_ = data_.drop(data_.columns[[1,3]], axis=1)
print(data_.to_csv("new_one.csv"))
#remove row
#by name
#data_row = data_row.drop(["row_labels_list"], axis = 0)->i dont have row label in this file

data_row = data_row.drop(data_row.index[[1,3]],axis=0)
print(data_row.to_csv("row.csv"))

#creat csv file

#creat grhaf from data

import matplotlib.pyplot as plt
import pandas as pd

purchas_list = data.Purchased.tolist()
estimatedSalary = data.EstimatedSalary.tolist()

# Assuming you have a DataFrame called 'data' with 'estimatedSalary' and 'purchased' columns
# Example data:
data = pd.DataFrame({
    'estimatedSalary': estimatedSalary,
    'purchased': purchas_list  # Binary indicator (0: not purchased, 1: purchased)
})

# Separate data based on 'purchased' status
not_purchased = data[data['purchased'] == 0]
purchased = data[data['purchased'] == 1]

# Create the plot
plt.scatter(not_purchased['estimatedSalary'], not_purchased['purchased'], color='red', label='Not Purchased')
plt.scatter(purchased['estimatedSalary'], purchased['purchased'], color='green', label='Purchased')

# Add labels and title
plt.xlabel('Estimated Salary')
plt.ylabel('Purchased')
plt.title('Relationship between Estimated Salary and Purchase')

# Show legend
plt.legend()

# Show the plot
plt.show()

