'''Function with Variable Number of Parameters: 
Write a function called sum_all that accepts an arbitrary 
number of parameters and returns their sum. 
Hint: You might want to look into how to use *args in Python.'''

def arbitrary(*args):
    total = sum(args)
    return total

result = arbitrary(-1,22,33,41,-6)
print(result)

# BENAR