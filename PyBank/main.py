import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

Months = []
Total_Profit_Loss = 0
Profit_Loss_Changes = []
Previous_Profit_Loss = None
greatest_increase = {"date": None, "amount": float("-inf")}
greatest_decrease = {"date": None, "amount": float("inf")}

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# The total number of months included in the dataset
# skip the header row
    
    header = next(csvreader)
    for row in csvreader:
        Date = row[0]
        Months.append(Months)
       
# The net total amount of "Profit/Losses" over the entire period
        profit_loss = int(row[1])
        Total_Profit_Loss += profit_loss

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
        if Previous_Profit_Loss is not None:
            change = profit_loss - Previous_Profit_Loss
            Profit_Loss_Changes.append(change)

# The greatest increase in profits (date and amount) over the entire period
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = Date
                greatest_increase["amount"] = change
# The greatest decrease in profits (date and amount) over the entire period
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = Date
                greatest_decrease["amount"] = change

        Previous_Profit_Loss = profit_loss

# average of above changes
Average_Change = sum(Profit_Loss_Changes) / len(Profit_Loss_Changes)

Total_Months =len(Months)

# printing all the output to the financial analysis on the terminal
print("Total Months:", Total_Months)
print("Total:", Total_Profit_Loss)
print("Average Change:", Average_Change)
print("Greatest Increase in Profits:")
print(f"Date: {greatest_increase['date']}, Amount: {greatest_increase['amount']}")
print("Greatest Decrease in Profits:")
print(f"Date: {greatest_decrease['date']}, Amount: {greatest_decrease['amount']}")

# exporting to a text file - done with the terminal by using:
# python main.py > FinancialAnalysis.txt









