import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Social_Network_Ads.csv')
ages = data.Age
salaries = data.EstimatedSalary

# Function to find the average salary between those ages
def avg_salary(start, end):
    ages_row = data[(data['Age'] >= start) & (data['Age'] <= end)]
    matched_salaries = ages_row['EstimatedSalary']
    avg_salary = matched_salaries.mean()
    return avg_salary

import matplotlib.pyplot as plt

# Define your age groups and average salaries
age_groups = ['20-30', '31-40', '41-50', '51-60', '61+']
average_salaries = [avg_salary(20, 30), avg_salary(31, 40), avg_salary(41, 50), avg_salary(51, 60), avg_salary(61, 10000000)]

plt.figure(figsize=(8, 5))
plt.bar(age_groups, average_salaries)
plt.xlabel('Age Group')
plt.ylabel('Average Salary')
plt.title('Bar Chart: Average Salaries Across Different Age Groups')
plt.xticks(rotation=45)
plt.show()

# Point plot
plt.figure(figsize=(8, 5))
plt.plot(age_groups, average_salaries, marker='o')
plt.xlabel('Age Group')
plt.ylabel('Average Salary')
plt.title('Point Plot: Average Salaries Across Different Age Groups')
plt.xticks(rotation=45)
plt.show()

# Line plot
plt.figure(figsize=(8, 5))
plt.plot(age_groups, average_salaries, marker='o', linestyle='-')
plt.xlabel('Age Group')
plt.ylabel('Average Salary')
plt.title('Line Plot: Average Salaries Across Different Age Groups')
plt.xticks(rotation=45)
plt.show()

# Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(age_groups, average_salaries)
plt.xlabel('Age Group')
plt.ylabel('Average Salary')
plt.title('Scatter Plot: Average Salaries Across Different Age Groups')
plt.xticks(rotation=45)
plt.show()


salaries_by_age_2 = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Plotting the scatter plot
plt.figure(figsize=(8, 5))
for i, salary in enumerate(salaries_by_age_2):
    plt.scatter([i] * len(age_groups), [salary] * len(age_groups))

plt.xlabel('Age Group')
plt.ylabel('Salary')
plt.title('Scatter Plot: Salaries Across Different Age Groups')
plt.xticks(range(len(salaries_by_age_2)), salaries_by_age_2)
plt.yticks(range(10000, 100001, 10000))  # Setting y-ticks from 10,000 to 100,000 with an interval of 10,000
plt.grid(True)
plt.show()