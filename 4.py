'''Function with Default Parameters: Write a function called power 
that takes two parameters: base and exponent. The function should return 
the result of raising the base to the power of the exponent.
If no exponent is provided when the function is called, the function
should assume an exponent of 2.'''

def power (base, exp=2):
    result = base**exp
    return result

pow = power(10)
print(pow)

# BENAR