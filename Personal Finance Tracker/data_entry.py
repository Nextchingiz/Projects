#Disclaimer
"""
In this file we will store all the functions related to getting
information from the user.
"""

#Import libraries
from datetime import datetime

#Main Functions

#Define first the date format we are looking for
date_format = "%d-%m-%Y"

#Define the possible actions for Category (Income or Expense)
CATEGORIES = {
    "I" : "Income",
    "E" : "Expense"
    }

#Get Date function, that will ask the user the date
def get_date(prompt, allow_default = False):

    date_str = input(prompt)

    if allow_default and not date_str:
        #Specify the format we want the date in(Day - Month - Year)
        return datetime.today().strftime(date_format)
    
    try:
        #We are taking the date string passed, and we try to convert it to the defined format
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format) #If it is a valid date, we convert it to our defined date format
    except ValueError:
        #If the date entered is not valid, we just repeat the same process again, until we get a valid date
        print("Invalid date format, please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)
    

#Get Amount function, that will ask the user the amount of money
def get_amount():

    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non - negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

#Get Category function, that will ask the user the category (Income or Expense)
def get_category():
    
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()

    if category in CATEGORIES:
        return CATEGORIES[category]
    else:
        print("Invalid category, please enter 'I' for Income or 'E' for Expense")
        return get_category() #Recursion


#Get Description function, that will ask the user for a description of the transaction
def get_description():
    return input("Enter a description (optional): ")