def data_type(x=None):

'''Define a function called data_type, to take one argument. Compare and return results, based on the argument supplied to the function. Complete the test to produce the perfect function that accounts for all expectations.

For strings, return its length.
For None return string 'no value'
For booleans return the boolean
For integers return a string showing how it compares to hundred e.g. For 67 return 'less than 100' for 4034 return 'more than 100' or equal to 100 as the case may be
For lists return the 3rd item, or None if it doesn't exist

'''
    
    #x = input("Enter your argument:")
    
    if x == None:
      return "no value"
      
    elif type(x) == list:
      if len(x) >= 3:
        return x[2]
      else:
        return None
            
    elif type(x) == str:
      return len(x)
    
    elif type(x) == int:
      if x < 100:
        return "less than 100"
      elif x > 100:
        return "more than 100" 
      else :
        return "equal to 100" 
            
    elif type(x) == bool:
      return x
            
#print data_type()