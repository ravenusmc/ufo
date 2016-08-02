#This function is for validation for user input. 
def valid(choice):
  if choice == 'y' or choice == 'n':
    return True 
  else:
    return False

def validMain(choice):
  if choice == 'help' or choice == 'next':
    return True
  else: 
    return False

def validStart(choice):
  if choice == 'city' or choice == 'state' or choice == 'shape' or choice == 'other':
    return True
  else:
    return False

