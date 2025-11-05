# Monthly savings calculator
monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your total monthly expenses:"))
interest = 0.05
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest)
print("Your monthly savings are ", "$"+str(monthly_savings))
print("Projected savings after one year, with interest, is ", "$"+str(projected_savings))
