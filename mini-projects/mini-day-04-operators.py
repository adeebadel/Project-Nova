#Requirements:
#Ask for:
#Hours worked
#Hourly rate
#Calculate:
#Total salary
#Then display a clean summary.
#Bonus: Ask how much tax (%) should be deducted and calculate the final salary.
hours = float(input("Hours worked :"))
rate = float(input("Enter amount :"))
tax_percent = float(input("Tax percentage :"))

total_salary = hours * rate
tax_amount = total_salary * (tax_percent / 100)
final_salary = total_salary - tax_amount

print("\nNumber of Hours :", hours)
print("Amount :", rate)
print("Gross Salary :", total_salary)
print("Tax Amount :", tax_amount)
print("Final Salary :", final_salary)