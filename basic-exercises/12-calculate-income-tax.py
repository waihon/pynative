def income_tax(income):
    income_tax = 0
    remaining = income
    
    if remaining >= 10_000:
        income_tax += 10_000 * 0.0
        remaining -= 10_000

    if remaining >= 10_000:
        income_tax += 10_000 * 0.10
        remaining -= 10_000

    income_tax += remaining * 0.20
    
    return income_tax

income = 45_000
print("Income tax for ${:.0f}: ${:.0f}".format(income, income_tax(income)))
