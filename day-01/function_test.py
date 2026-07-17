# Function - reusable block of code
def sum_of_num():
    num1 = int(input("Enter num 1: "))
    num2 = int(input("Enter num 2: "))
    sum = num1+num2
    print(sum)

sum_of_num()

def take_backup():
    print("Backup script started...")


day = input("Enter the Day: ")
if (day == "Monday"):
    take_backup()