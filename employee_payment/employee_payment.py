#Defining Parameters
min_hours_worked = 0
max_hours_worked = 40
min_hourly_rate = 12.50
max_hourly_rate = 150.00
gross_range1 = 300.00
gross_range2 = 300.01
gross_range3 = 400.00
gross_range4 = 400.01
gross_range5 = 500.00
gross_range6 = 500.01

withholding_1 = 0.1
withholding_2 = 0.12
withholding_3 = 0.15
withholding_4 = 0.20

withholding_tax = 0
continue_program = "y"


while continue_program == "y":

# Accepts User input
    hours_worked = float(input("Enter the number of hours worked: "))
    hourly_rate = float(input("Enter the hourly pay rate: "))

# Assignment of formulas to be used
    gross_pay = float(hours_worked * hourly_rate)
    net_pay = float(gross_pay - withholding_tax)

# Creates a break
    print("\n\n")

# Code to Calculate the withholding tax
    if gross_pay <= gross_range1:
        withholding_tax = withholding_1 * gross_pay
    elif gross_pay >= gross_range2 and gross_pay <= gross_range3:
        withholding_tax = withholding_2 * gross_pay
    elif gross_pay >= gross_range4 and gross_pay <= gross_range5:
        withholding_tax = withholding_3 * gross_pay
    elif gross_pay >= gross_range6:
        withholding_tax = withholding_4 * gross_pay

    # Checks condition to carry out the code 
    if hours_worked < min_hours_worked or hours_worked > max_hours_worked:
        print("Hours worked should not be more than" + \
              " 40 hours per week and should not be less than 0.")

    elif hourly_rate < min_hourly_rate or hourly_rate > max_hourly_rate:
        print("Minimum hourly rate is $12.50 per hour" + \
              " and maximum is $150.00 per hour")

# Prints the results
    else:
        print("Gross pay is", gross_pay)
        print("Witholding tax is", withholding_tax)
        print("Net Pay is", net_pay)
# Creates space for subsequent operations 
        print("\n\n\n")
        
    continue_program = input("Do you want to perform another transaction?" +\
                             " (Enter y for yes): ")