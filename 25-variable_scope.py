#scope = The region that a variable is recognized
#LEGB Rule
name = "Bro" # global scope

def display_name():
    name = "Code" # local scope
    print(name)
    
display_name()