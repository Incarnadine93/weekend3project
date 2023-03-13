import math

def inputnumber(message): # function to confirm input is integer
  while True:
    try:
        userInput = int(input(message)) # taking input
    except ValueError:
        print("Not an integer! Try again.") # disapproving of input
        continue
    else:
        return userInput # approving of input
    
def inputstring(message): # function to confirm input is string
    while True:
        try:
            userInput = str(input(message)) # taking input
        except ValueError:
            print("Not a string! Try again.") # disapproving of input
            continue
        else:
            return userInput # approving of input

class option: # object for user to go through options
    def menu():
        x = inputstring('What would like you to do?\n     "I" for Income options\n     "E" for Expenses options\n     "R" for Roi options\n     "Q" for Quit and view roi ') # initial menu options
        if x.lower() == 'i':
            y = inputstring('"A" for adding income information\n"R" to remove a source of income\n"T" to show total monthly income. ') # sub menu options
            if y.lower() == 'a':
                name.get()
            elif y.lower() == 'r':
                name.total()
                name.remove()
            elif y.lower() == 't':
                name.total()
                option.menu()
            else:
                print("That is not one of the options.") # if response is invalid
                option.menu()
        elif x.lower() == 'e':
            y = inputstring('"A" for adding expense information\n"R" to remove a source of expense\n"T" to show total monthly expense. ') #sub menu
            if y.lower() == 'a':
                name2.get()
            elif y.lower() == 'r':
                name2.total()
                name2.remove()
            elif y.lower() == 't':
                name2.total()
                option.menu()
            else:
                print("That is not one of the options.") # if response is invalid
                option.menu()
        elif x.lower() == 'r':
            y = inputstring('"A" for adding cash on cash information\n"R" to remove a source of cash on cash\n"T" to show total cash on cash flow. ') #sub menu
            if y.lower() == 'a':
                name3.get()
            elif y.lower() == 'r':
                name3.total()
                name3.remove()
            elif y.lower() == 't':
                name3.total()
                option.menu()
            else:
                print("That is not one of the options.") # if response is invalid
                option.menu()
        elif x.lower() == 'q':
            cash_flow()
        else:
                print("That is not one of the options.") # if response is invalid for primary menu
                option.menu()
                
class income: # object for adjusting income dictionary
    def __init__(self):
       self.inc = {} # setting initial value to income idctionary
       self.inc_rv = None # setting inital value to income rent value
    def get(self):
        if self.inc_rv == None: # if rent/value isnt set yet
            self.inc_rv = inputnumber("How much will be charged for rent on this property per month?: ")
            self.inc["Rent"] = self.inc_rv # adding user input to rent value
        else: # if rent/value is already set
            self.inc_k = inputstring("What else are you charging on this property?: ")
            self.inc_v = inputnumber("How much will be charged for this service/amenity?: ")
            self.inc[self.inc_k.title()] = self.inc_v # adding key/value to dicitonary based on user input
        option.menu() # returning to menu
    def remove(self):
        if self.inc == None: # If not information has been logged to income dictionary
            print("No information logged to remove.")
        else:
            self.inc_r = inputstring("What source of income would you like to remove?: ")
            if self.inc_r.title() not in self.inc: #confirming if key is even in dictionary
                print("That is not in income data")
            else:    
                del self.inc[self.inc_r.title()] # removing key from dictionary
        option.menu() # returning to menu
    def total(self): # outputting all income data and summing it together
        print("Income Source                              Amount") 
        print("-------------------------------------------------")
        total_i = 0
        for key, value in self.inc.items():
            length = len(key)
            space = (" " * (45-length))
            print(f"{key}{space}${value}")
            total_i += float(value)
        print(f"Monthly Total: ${total_i}\n")
        return total_i # returning value of total monthly income

class expenses: # object for adjusting expenses dictionary
    def __init__(self):
       self.exp = {} # setting inital value to expenses dictionary
       self.exp_tv = None # setting initial value to expenses tax value
    def get(self): # add function
        if self.exp_tv == None: # if tax/value isnt set yet
            self.exp_tv = inputnumber("How much is propery tax on this property per month?: ")
            self.exp["Tax"] = self.exp_tv # adding user input to rent value
        else: # if tax/value is already set
            self.exp_k = inputstring("What else are you paying for on this property?: ")
            self.exp_v = inputnumber("How much are you paying for this expense?: ")
            self.exp[self.exp_k.title()] = self.exp_v # adding key/value to dictionary based on user input
        option.menu() # returning to menu
    def remove(self):
        if self.exp == None: # If no information has been logged to expenses dictionary
            print("No information logged to remove.")
        else:
            self.exp_r = inputstring("What expense would you like to remove?: ")
            if self.exp_r.title() not in self.exp: #confirming if key is even in dictionary
                print("That is not in the expenses data")
            else:    
                del self.exp[self.exp_r.title()] # removing key from dictionary
        option.menu() # returning to menu
    def total(self): # outputting all income data and usmming it together
        print("Expense source                             Amount") 
        print("-------------------------------------------------")
        total_e = 0
        for key, value in self.exp.items():
            length = len(key)
            space = (" " * (45-length))
            print(f"{key}{space}${value}")
            total_e += float(value)
        print(f"Monthly Total: ${total_e}\n")
        return total_e # returning value of total monthly expenses

class cash_flow:
    def __init__(self):
        self.cocRoi = None # setting inital value to cocRoi
        total_c = (name.total() - name2.total())*12 # (income - expenses) * 12
        self.cocRoi = total_c / name3.total()
        self.cocRoi = self.cocRoi * 100
        print(f"% {self.cocRoi} is the total annual roi")
    def __str__(self):
        return self.cocRoi
        
class roi: # object for adjusting initial investment
    def __init__(self):
       self.roi = {} # setting inital value to roi dictionary
       self.roi_dv = None # setting initial value to income rent value
    def get(self): # add function
        if self.roi_dv == None: # if down/value isnt set yet
            self.roi_dv = inputnumber("How much did you put down for the property?: ")
            self.roi["Down payment"] = self.roi_dv #adding key/value to dictionary
        else: # if information has been logged
            self.roi_k = inputstring("What else did you put down for the initial cost of the property?: ")
            self.roi_v = inputnumber("How much are you paying for this cost: ")
            self.roi[self.roi_k.title()] = self.roi_v # adding key/value to dictionary
        option.menu() # returning to menu
    def remove(self):
        if self.roi == None: # if no information has been logged to roi dictionary
            print("No information logged to remove.")
        else: # if information has been logged
            self.roi_r = inputstring("What inital cost would you like to remove?: ")
            if self.roi_r.title() not in self.roi: #confirming if key is even in dictionary
                print("That is not in the inital cost data")
            else:    
                del self.roi[self.roi_r.title()] # removing key from dictionary
        option.menu() # returning to menu
    def total(self): # outputting all roi data and summing it together
        print("Inital investment source                   Amount") 
        print("-------------------------------------------------")
        total_r = 0
        for key, value in self.roi.items():
            length = len(key)
            space = (" " * (45-length))
            print(f"{key}{space}${value}")
            total_r += float(value)
        print(f"Total: ${total_r}\n")
        return total_r # returning value of total initial investment

print("Welcome to the Rental Property Calculator")
name = income()
name2 = expenses()
name3 = roi()
option.menu()
