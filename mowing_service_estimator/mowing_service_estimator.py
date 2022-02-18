#Standard Fees
standard_lawn_area1 = 4000
standard_lawn_area2 = 6000
weekly_fee = 0

continue_program = "y"

while continue_program == "y":
# Collects user input
    lawn_length = float(input("Enter the length of the lawn: "))

    lawn_width = float(input("Enter the width of the lawn: "))

# performs the area of the lawn
    area_of_lawn = lawn_length * lawn_width

# Prints the cost out for the user to see
    print("The Area of the lawn is:", area_of_lawn)
    if area_of_lawn < standard_lawn_area1:
        weekly_fee = 25
        print("The weekly fee for mowing the lawn is $%.2f"% 25)
    elif area_of_lawn >= standard_lawn_area1 and area_of_lawn < standard_lawn_area2:
        weekly_fee = 35
        print("The weekly fee for mowing the lawn is $%.2f"% 35)
    elif area_of_lawn >= standard_lawn_area2:
        weekly_fee = 50
        print("The weekly fee for mowing the lawn is $%.2f"% 50)

# Seasonal fee paid for the service for a period of 20 weeks
    seasonal_fee = weekly_fee * 20
    print("The seasonal fee for mowing the lawn is $%.2f"% seasonal_fee)
# Creates space for subsequent operations   
    print("\n\n")

#Allows for another calculation
    continue_program = input("Do you want to perform another transaction?" +\
                        " (Enter y for yes): ")