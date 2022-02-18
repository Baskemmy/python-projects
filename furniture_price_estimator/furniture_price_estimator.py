continue_program = "y"

while continue_program == "y":
# Instruction manual for users
    print("--Pick a material for your table--")
    print("Choose 1 for Pine, 2 for Oak, or 3 for Mahogany")
# Prompts the user to enter their choice
    wood_type = input("Enter your choice: ")
# Defines the cost for each wood type
    pine_cost = 100
    oak_cost = 200
    mahogany_cost = 300

# Code block for the program
    if wood_type == "1":
        print("Cost of chosen wood type is $%.2f."% pine_cost)
    elif wood_type == "2":
        print("Cost of chosen wood type is $%.2f."% oak_cost)
    elif wood_type == "3":
        print("Cost of chosen wood type is $%.2f."% mahogany_cost)
    else:
        print("Invalid Choice!")
# Creates space for subsequent operations 
    print("\n\n")

    continue_program = input("Do you want to check out another wood type?" +\
                        " (Enter y for yes and n for no): ")
        