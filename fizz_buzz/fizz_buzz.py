#Determines whether a number is a Fizz, a Buzz or just a number and returns what the number is.
def fizz_buzz(num):

'''Create a function fizz_buzz to return 'Fizz', 'Buzz', 'FizzBuzz', or the argument it receives, 
all depending on the argument of the function, a number that is divisible by, 3, 5, or both 3 and 5, respectively.

When the number is not divisible by 3 or 5, the number itself should be returned.
'''
  
  if (num % 5 == 0 and num % 3 == 0):
    return "FizzBuzz"
    
  elif (num % 3) == 0:
    return "Fizz"
    
  elif (num % 5) == 0:
    return "Buzz"
    
  else:
    return num
