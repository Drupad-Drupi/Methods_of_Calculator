# Nested If Simple Calculator using match-case (Python 3.10+)
while True:  # loop condition
    # Selection for operation
    option = int(input("Enter the value for\n 1-->Addition \n 2-->Subtraction \n 3-->Multiplication \n 4-->Division \n 5-->Exit \n Option: "))
    if option == 5:
        print("Exiting the calculator.")
        break
    # Inputting the values for the operation
    n1 = float(input("Enter the first value: "))
    n2 = float(input("Enter the second value: "))
    match option:
        case 1:
            print("Sum of",n1 ,"+", n2,"=",n1+n2)
        case 2:
            print("Diff of",n1,"-",n2,"=",n1-n2)
        case 3:
            print("Product of",n1,"*",n2,"=",n1*n2)
        case 4:
            if n2==0:  # for avoiding ZeroDivisionError
                print("Error: Division by zero is not allowed.")
            else:
                print("Quotient of ",n1,"/",n2,"=",n1/n2)
        case default:
            print("Invalid option. Please choose a valid option.")
    ch = input("Do you want to continue? (y/n): ")
    if ch.lower()==n:  # To handle the exit condition
        print("Exiting the calculator.")
        break
