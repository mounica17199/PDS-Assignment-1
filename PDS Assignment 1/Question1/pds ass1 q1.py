#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import matplotlib.pyplot as plt

# Read the raw data
raw_data = pd.read_csv(r"C:/Users/91830/Downloads/first_question.csv")

# Remove rows with NA values and "N" values
clean_data = raw_data.dropna()
clean_data = clean_data[clean_data != "N"].dropna()

# Write clean data to a new CSV file
clean_data.to_csv(r"C:/Users/91830/Downloads/clean_data.csv", index=False)

# Load clean data
print(clean_data)

# Check the data type of the 'Height (Inches)' column
print(type(clean_data['Height (Inches) ']))
# Summarize the clean data
print(clean_data.describe())

# Save the summary to a text file
with open(r"C:/Users/91830/Downloads/results.txt", "w") as file:
    file.write(str(clean_data.describe()))

## Plotting Age against frailty
plt.bar(clean_data['Age'], clean_data['Grip Strength'], color='green')
plt.xlabel('Age')
plt.ylabel('Grip Strength')
plt.title('Age vs Grip Strength')
plt.show()


# In[ ]:




