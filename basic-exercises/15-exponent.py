def exponent(base, exp):
    print("base =", base)
    print("exponent =", exp)
    
    result = base ** exp
    expr = (str(base) + " * ") * (exp - 1) + str(base) + " = " + str(result)
    
    print(base, "raises to the power of", exp, ":", result, "i.e. (", expr, ")")

exponent(2, 5)
exponent(5, 4)
