#!/usr/bin/env python
# coding: utf-8

# # Coding Set 4
# ## Algorithm Workbench

# In[3]:


number = 0 #set number to 0
while number <= 1000: #start the loop to check and see if the number is less than 1000
    print(number) #prints the number
    number += 10 #add ten then starts over


# In[5]:


print("Welcome to the Money counter! Just enter your 10 latest numbers, and we will give you your running total")

total = 0  # Initialize the total to 0

for i in range(10):
    number = float(input(f"Enter the {i+1}st amount: "))  # Prompt the user for each amount
    total += number  # Add the entered amount to the total

print("Running Total:", total)  # Display the final running total


# ## Programming exercises

# In[ ]:


name = input("Thank you for using the Bug Counter! Please enter your name: ")

bugs = 0  # Set the bug count to 0

for day in range(5):
    amount = float(input(f"Enter the {day + 1}st amount: "))  # Ask 5 times how many bugs
    bugs += amount  # Add all of the numbers together

print("Total:", bugs)


# In[ ]:


AMOUNT_OF_YEARS = int(input("How many years would you like to add?"))  # Get the number of years from the user
total_yearly_avg = 0  # set the total yearly average to 0

for year in range(AMOUNT_OF_YEARS):
    year_total = 0  # Set the year total to 0

    for month in range(12):
        rain = float(input(f"Enter the average rainfall for month {month + 1}: ")) #give input but also addes number to each month
        year_total += rain  # Add the monthly rainfall to the year total

    year_avg = year_total / 12  # Calculate the yearly average
    print(f"Year {year + 1} average rainfall: {year_avg:.2f} inches")

    total_yearly_avg += year_avg  # Add the yearly average to the total

average_over_years = total_yearly_avg / AMOUNT_OF_YEARS  # Calculate the average over the all the years
print(f"Average over {AMOUNT_OF_YEARS} years: {average_over_years:.2f} inches")


# In[ ]:




