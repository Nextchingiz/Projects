#Disclaimer
"""
Name: Chingizkhan Nurbolatov Yankolov
Date: February 2025
Description: This project is a "Personal Finance Tracker", used to track and manage your expenses.
In this project we will be makinguse of various libraries and functions useful for data management.
"""

#Import libraries
import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description
import matplotlib.pyplot as plt

#Setting up classes

#CSV Class
class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def intialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns = cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index = False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date" : date,
            "amount" : amount, 
            "category" : category,
            "description" : description
        }
        
        with open(cls.CSV_FILE, "a", newline = "") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE) #Read as a data frame
        df["date"] = pd.to_datetime(df["date"], format = CSV.FORMAT) #Take the date time and convert to date time object
        start_date = datetime.strptime(start_date, CSV.FORMAT) #Do the same with the start date
        end_date = datetime.strptime(end_date, CSV.FORMAT) #Do the same with the end date

        mask = (df["date"] >= start_date) & (df["date"] <= end_date) #Create a mask that will filter the rows inside our data frame
        filtered_df = df.loc[mask] #Apply the data mask

        if filtered_df.empty: #If it is empty, there are no transactions, so we print out that there is nothing
            print("No transactions found in the given date range")
        else: 
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index = False, formatters = {"date": lambda x: x.strftime(CSV.FORMAT)}))

            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}")
        
        return filtered_df

#Define the function that will add the user input into our CSV file
def add():
    CSV.intialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ", allow_default = True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

def plot_transactions(df):
    df.set_index('date', inplace = True)
    
    income_df = df[df["category"] == "Income"].resample("D").sum().reindex(df.index, fill_value = 0)
    expense_df = df[df["category"] == "Expense"].resample("D").sum().reindex(df.index, fill_value = 0)

    plt.figure(figsize = (10, 5))
    plt.plot(income_df.index, income_df["amount"], label = "Income", color = "green")
    plt.plot(expense_df.index, expense_df["amount"], label = "Expense", color = "red")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()


#Define the function that will ask the user for the information on the date of the transaction, to view it
def main():

    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1 - 3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the start date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if input("Do you want to see a plot? (y/n) ").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            print("Exiting")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")

if __name__ == "__main__":
    main()