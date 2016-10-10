def data_type(x=None):
    
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