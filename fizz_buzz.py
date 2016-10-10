#Determines whether a number is a Fizz, a Buzz or just a number and returns what the number is.
def fizz_buzz(num):
  
  if (num % 5 == 0 and num % 3 == 0):
    return "FizzBuzz"
    
  elif (num % 3) == 0:
    return "Fizz"
    
  elif (num % 5) == 0:
    return "Buzz"
    
  else:
    return num
