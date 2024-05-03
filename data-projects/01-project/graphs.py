import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Social_Network_Ads.csv')

#this function find the avg salari between those ages
def avg_salary(start, end):
    ages_row = data[(data['Age'] >= start) & (data['Age'] <= end)]
    matched_salaries = ages_row['EstimatedSalary']
    avg_salary = matched_salaries.mean()
    return avg_salary

age_groups = ['20-30', '31-40', '41-50', '51-60', '61+']  # Define your age groups
average_salaries = [avg_salary(20,30),avg_salary(31,40), avg_salary(41,50), avg_salary(51,60), avg_salary(61,10000000)]

# Plotting
plt.bar(age_groups, average_salaries)
plt.xlabel('Age Group')
plt.ylabel('Average Salary')
plt.title('Comparison of Average Salaries Across Different Age Groups')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability if necessary
plt.show()
