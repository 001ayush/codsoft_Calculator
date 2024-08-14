first_num = float(input("Enter First Number = "))
Second_num = float(input("Enter Second Number = "))
op = input("Enter Operation('+','-','*','/') To Perform = ")
if op == '+':
    print("Sum Is ",first_num+Second_num)

elif op == '*':
    print("Product Is ",first_num*Second_num)

elif op == '-':
    print("Subtraction Is ",first_num-Second_num)

elif op == '/':
    print("result Is ",first_num/Second_num)

else:
    print("Invalid Input")

