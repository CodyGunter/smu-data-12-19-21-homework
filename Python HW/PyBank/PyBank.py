import csv


csvpath = "PyBank/Resources/budget_data.csv"
rows = []

totalMonths = 0
totalProfit = 0

changes = []
monthchg = []
prevMargain = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    for row in csvreader:
        rows.append(row)
        
        totalMonths += 1
        totalProfit += int(row[1])
        
        if totalMonths > 1:
            change = int(row[1]) - prevMargain 
            changes.append(change)
            monthchg.append(row[0])

        prevMargain = int(row[1])

    
    print("Financial Analysis")
    print("---------------------")
    print(f'Total Months: {len(rows)}')
    print(f'Total Profit: {totalProfit}')
    print(f'Average Profit Loss: {sum(changes) / len(changes)}')
   

    maxMonth_idx = changes.index(max(changes))
    maxMonth = monthchg[maxMonth_idx]
    minMonth_idx = changes.index(min(changes))
    minMonth = monthchg[minMonth_idx]
    
    print(f'Max Profit Gain: {maxMonth} $ {max(changes)}')
    print(f'Max Profit Loss: {minMonth} $ {min(changes)}')



    

    