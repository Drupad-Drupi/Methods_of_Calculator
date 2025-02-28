# adds two numbers
def sum(x,y):
    return x+y
# subtracts two numbers
def diff(x,y):
    return x-y
#  multiplies two numbers
def mult(x,y):
    return x*y
# divides two numbers
def div(x,y):
    return x/y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    # take input from the user
    c=input("Enter choice(1/2/3/4):")
    # check if choice is one of the four options
    if c in ('1', '2', '3', '4'):
        try:
            a = float(input("Enter the value of 1st:"))
            b= float(input("Enter the value of 2nd:"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if c=='1':
            print(a,"+",b,"=",sum(a,b))
        elif c=='2':
            print(a,"-",b,"=",diff(a,b))
        elif c=='3':
            print(a,"*", b,"=",mult(a,b))
        elif c=='4':
            print(a,"/",b,"=",div(a,b))
        # check if user need another calculation
        # break the loop if answer is no
        cal= input("Let's do next calculation? (y/n): ")
        if cal=="n":
          break
    else:
        print("Invalid Input")
