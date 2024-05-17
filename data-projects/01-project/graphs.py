import pandas as pd

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

# Line plot
plt.figure(figsize=(8, 5))
plt.plot(age_groups, average_salaries, marker='o', linestyle='-')
plt.xlabel('Age Group')
plt.ylabel('Average Salary')
plt.title('Line Plot: Average Salaries Across Different Age Groups')
plt.xticks(rotation=45)
plt.show()



salaries_by_age_2 = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# graphs about perches vs each relevant column

#1 purches vs age
df = pd.DataFrame(data)

# Function to calculate percentage of people purchasing within an age range
def percentage_Purchasing(start, end):
    ages_row = df[(df['Age'] >= start) & (df['Age'] <= end)]
    purchased = ages_row['Purchased'].sum()
    total_people = len(ages_row)
    if total_people == 0:  # Check if there are no people in the age range
        return 0
    return (purchased / total_people) * 100

# Age groups
age_groups = ['20-30', '31-40', '41-50', '51-60']

# Calculate percentage of people purchasing in each age group
percentage_purchased = [percentage_Purchasing(20, 30),
                        percentage_Purchasing(31, 40),
                        percentage_Purchasing(41, 50),
                        percentage_Purchasing(51, 60)]

# Create DataFrame for pie chart
pie_data = pd.DataFrame({'Age Group': age_groups, 'Percentage Purchasing': percentage_purchased})

# Plotting
plt.figure(figsize=(8, 6))
plt.pie(pie_data['Percentage Purchasing'], labels=pie_data['Age Group'], autopct='%1.1f%%', startangle=140)
plt.title('Percentage of People Purchasing by Age Group')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Calculate percentages
male_purch = len(df[(df['Gender'] == 'Male') & (df['Purchased'] == 1)])
male_not_purch = len(df[(df['Gender'] == 'Male') & (df['Purchased'] == 0)])
female_purch = len(df[(df['Gender'] == 'Female') & (df['Purchased'] == 1)])
female_not_purch = len(df[(df['Gender'] == 'Female') & (df['Purchased'] == 0)])

total_purchases = male_purch + female_purch
total_individuals = len(df)

percentage_male_purch = (male_purch / total_purchases) * 100
percentage_female_purch = (female_purch / total_purchases) * 100
percentage_male_not_purch = (male_not_purch / total_individuals) * 100
percentage_female_not_purch = (female_not_purch / total_individuals) * 100

# Data for pie chart
labels = ['Male Purchases', 'Female Purchases', 'Male Non-Purchases', 'Female Non-Purchases']
sizes = [percentage_male_purch, percentage_female_purch, percentage_male_not_purch, percentage_female_not_purch]
colors = ['blue', 'pink', 'lightblue', 'lightpink']
explode = (0.1, 0, 0, 0)  # explode 1st slice (Male Purchases)

# Plot pie chart
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Percentage of Purchases by Gender')

# Plot bar chart
plt.subplot(1, 2, 2)
plt.bar(['Male', 'Female'], [male_purch, female_purch], color=['blue', 'pink'])
plt.title('Number of Purchases by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Purchases')

plt.tight_layout()
plt.show()