class students: # Making a class
    name = "Raj" # Since, all the attributes are inside the class including function they must be intented
    standard = 11
    total_grade = 92 
    def __init__(self):
        print("This is a non-parameterized constructor")
    def display_details(self): # Creating a function inside of a class(don't forget to intend it to the same level as the attributes)
        print(self.standard)

# Displaying the attributes of a class using objects(IMPORTANT STEP!!!)
obj = students() # Making an object
obj1 = students()