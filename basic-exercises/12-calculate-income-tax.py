def income_tax(income):
    income_tax = 0
    remaining = income
    
    limit = [ 10_000, 10_000, 9_999_999 ]
    rates = [ 0.0, 0.10, 0.20 ]
    size = len(limit)
    
    for i in range(size):
        taxable_income = min(remaining, limit[i])
        income_tax += taxable_income * rates[i]
        remaining -= taxable_income
        if remaining <= 0:
            return income_tax
    
    return income_tax

incomes = [9_999, 10_000, 19_999, 20_000, 45_000]
for income in incomes:
    print("Income tax for ${:.0f}: ${:.2f}".format(income, income_tax(income)))
