def tax_cal(sub_total):
  tax_salary = sub_total * 0.15
  return tax_salary

def Final_salary():
  salary = float(input("Enter your base salary: "))
  bouns = float(input("How much bouns did you get?: "))
  sub_total = salary + bouns
  #sub_total = salary + float(input("How much bouns did you get? ")) 
  tax = tax_cal(sub_total)
  total = sub_total - tax
  print(f"Final salary after tax: {total} SAR")

Final_salary()