#This function is for validation for user input. 
def valid(choice):
  if choice == 'y' or choice == 'n':
    return True 
  else:
    return False

def validMain(choice):
  if choice == 1 or choice == 2 or choice == 3:
    return True
  else: 
    return False

def validStart(choice):
  if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6:
    return True
  else:
    return False

def validyearGraph(option):
  if option == 1 or option == 2:
    return True
  else:
    return False

