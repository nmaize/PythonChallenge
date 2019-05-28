# Dependencies
import csv
import os

# Load and output files
loadfile = os.path.join("Resources", "budget_data.csv")
outputfile = os.path.join("Resources", "budget_analysis.txt")

#Create variables for calculations
months = 0
month_of_change = []
net_change_list = []
PL_increase = ["", 0]
PL_decrease = ["", 9999999999999999999]
total_net = 0

# Read the csv and convert into list of dictionaries
with open(loadfile) as raw_data:
    readfile = csv.reader(raw_data)

    # Read header row
    headrow = next(readfile)

    # Appending first row 
    row = next(readfile)
    months = months + 1
    total_net = total_net + int(row[1])
    prev_net = int(row[1])

    for row in readfile:

        # Adding the total months
        months = months + 1
        total_net = total_net + int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate the greatest increase
        if net_change > PL_increase[1]:
            PL_increase[0] = row[0]
            PL_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < PL_decrease[1]:
            PL_decrease[0] = row[0]
            PL_decrease[1] = net_change

# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

#Summary - Print
results = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {PL_increase[0]} (${PL_increase[1]})\n"
    f"Greatest Decrease in Profits: {PL_decrease[0]} (${PL_decrease[1]})\n")

# Print the output (to terminal)
print(results)

# Export the results to text file
with open(outputfile, "w") as txt_file:
    txt_file.write(results)
