# finance calculator 

#User Input for Financial Details:
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#calculate monthly savings 

monthly_savings = monthly_income - monthly_expenses

#projected annual savings at rate of 5%

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output results
print(f"Your monthly savings are {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {projected_savings}")
