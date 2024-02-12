#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
student_data = pd.read_csv("C:/Users/91830/Downloads/StudentsPerformance.csv")

# Task 1: Box plot of Math Score by Gender
plt.figure(figsize=(8, 6))
sns.boxplot(x='gender', y='math score', data=student_data)
plt.xlabel('Gender')
plt.ylabel('Math Score')
plt.title('Math Score Distribution by Gender')
plt.savefig("C:/Users/91830/Downloads/math_score_gender_boxplot.jpg")
plt.show()

# Task 2: Scatter plot of Reading Score vs. Writing Score
plt.figure(figsize=(8, 6))
sns.scatterplot(x='reading score', y='writing score', hue='gender', data=student_data)
plt.xlabel('Reading Score')
plt.ylabel('Writing Score')
plt.title('Reading Score vs. Writing Score')
plt.savefig("C:/Users/91830/Downloads/reading_writing_score_scatterplot.jpg")
plt.show()

# Task 3: Violin plot of Math Score by Race/Ethnicity
plt.figure(figsize=(10, 6))
sns.violinplot(x='race/ethnicity', y='math score', data=student_data)
plt.xlabel('Race/Ethnicity')
plt.ylabel('Math Score')
plt.title('Math Score Distribution by Race/Ethnicity')
plt.savefig("C:/Users/91830/Downloads/math_score_race_violinplot.jpg")
plt.show()

# Task 4: Count plot of Test Preparation Course Completion by Gender
plt.figure(figsize=(8, 6))
sns.countplot(x='test preparation course', hue='gender', data=student_data)
plt.xlabel('Test Preparation Course Completion')
plt.ylabel('Count')
plt.title('Test Preparation Course Completion by Gender')
plt.savefig("C:/Users/91830/Downloads/test_prep_course_completion_countplot.jpg")
plt.show()
# Task 5: Bar plot of Average Scores by Parental Level of Education
parental_education_means = student_data.groupby('parental level of education').agg({'math score': 'mean', 'reading score': 'mean', 'writing score': 'mean'}).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='parental level of education', y='math score', data=parental_education_means)
plt.xlabel('Parental Level of Education')
plt.ylabel('Average Math Score')
plt.title('Average Math Scores by Parental Level of Education')
plt.xticks(rotation=45)
plt.savefig("C:/Users/91830/Downloads/average_math_scores_parental_education_barplot.jpg")
plt.show()


# In[ ]:





# In[ ]:




