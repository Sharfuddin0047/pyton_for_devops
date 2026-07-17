#Get the Environment from user and print it
for i in range(5):

    env = input("Enter the Environment: ") #Taking input from user
    print("The user env is:",env)


    # conditional statement
    if(env=="prd"):
        print("Don't deploy on Friday \n")
    elif(env == "stg"):
        print("Take backup and check the Application")
    elif(env == "test"):
        print("Test it well")
    else:
        print("Safe to deploy")

print()
# Type Casting - conversion of one data into another
a = int(input("Enter the num1: "))
b = int(input("Enter the num2: "))

print("Multiplication is: ",a*b)
print("Addition is: ",a+b)
print("Subtraction is: ",a-b)
print("Division is: ",a/b)