import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

titanic_data = pd.read_csv("data science folder\\titanic.csv")
print(titanic_data.head(),"\n")

print(titanic_data.columns,'\n')

#group data by gender to get counts and average fare
gender_counts = titanic_data["Sex"].value_counts()
print(f'\n Gender counts: \n {gender_counts} \n')

#average fare per gender
avg_fare_by_gender = titanic_data.groupby("Sex")["Fare"].mean()
print(f"\n average fare by gender: \n {avg_fare_by_gender}\n")

#class distribution for pychart
class_distribution = titanic_data["Pclass"].value_counts()
print(f"\n class distribution:\n {class_distribution}\n ")

#making pychart
plt.figure(figsize=(9,5)) #9=w 5=h so (w,h)
plt.subplot(131)

plt.bar(gender_counts.index,gender_counts.values,color=["blue","pink"])
plt.title("total number of men and women")
plt.xlabel("Gender")
plt.ylabel("Count")
#plt.show()


#bar graph for average fare by gender
plt.subplot(132)
plt.bar(avg_fare_by_gender.index,avg_fare_by_gender.values,color=["brown","pink"])
plt.title("average fare for men and women")
plt.xlabel("Gender")
plt.ylabel("average fare")
#plt.show()

#pie chart for class distribution
plt.subplot(133) # can also be written as plt.subplot(1,3,3)
plt.pie(class_distribution,labels=class_distribution.index,autopct='%1.2f%%',startangle=90)
plt.title("Passenger Class Distribution")
plt.tight_layout()
plt.show()

#subplots
# the first number from represents the number of graphs in a section
# the second number is the maximum number of graphs to be shown
# the third number is the order in which the graphs are shown

