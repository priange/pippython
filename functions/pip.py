
#        In the math.py module, define these additional 5 functions;
# addition
# subtract
# divide
# multiply
# remainder
# Each function accepts two arguments and returns the appropriate output.

# On your interpreter invoke each function 3 times with different arguments. 
def addition (a,b):
    result1 = a+b
    return result1

def subtraction(a,b):
    result2=a-b
    return result2

def modulus(a,b):
    result3=a%b
    return result3

def division(a,b):
    result4=a/b
    return result4

def multiplication(a,b):
    result5=a*b
    return result5


#     A function named concatenate_args that takes any number of string arguments 
# in positional arguments format and concatenates them into a single string
  
def concatenate_args(String1,String2):
    rest= String1+String2
    return rest
