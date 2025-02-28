# Nested If Simple Calculator
while True: #loop condition
    # Selection for operation
    option = int(input("Enter the value for\n 1-->Addition \n 2-->Subtraction \n 3-->Multiplication \n 4-->Division \n 5-->Exit \n Option: "))
    if option == 5:
        print("Exiting the calculator.")
        break
    #Inputing the values for the operation
    n1 = float(input("Enter the first value: "))
    n2 = float(input("Enter the second value: "))
    # Operation for Addition
    if option == 1:
        print("Sum of",n1,"+",n2,"=",n1+n2)
    # Operation for Subtraction
    if option == 2:
        print("Difference of",n1,"-",n2,"=",n1-n2)
    # Opertaion for Multiplication
    if option == 3:
        print("Product of",n1,"*",n2,"=",n1*n2)
    # Operation for Division
    if option == 4:
        if n2 == 0: # for avoiding ZeroDivisionError
            print("Error: Division by zero is not allowed.")
        if n2!=0: 
            print("Quotient of", n1,"/",n2,"=",n1/n2)
    if option <1 or option >=5: #To handle invalid inputs
        print("Invalid option. Please choose a valid option.")
    ch = input("Do you want to continue? (y/n): ")
    if ch.lower() == 'n': # To handle the exit condition
        print("Exiting the calculator.")
        break
    if ch.lower() == 'y':
        continue
