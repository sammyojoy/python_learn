# operation_sign = input("please what operation sign do you want to use? ")
# number_1 = float(input("give me your first number") )
# number_2 = float(input("give me your second number") )

# if operation_sign == '+':
#     print(number_1 + number_2)
# elif operation_sign == '-':
#     print(number_1 - number_2)
# elif operation_sign == '*':
#     print(number_1 * number_2)
# elif operation_sign == '/':
#     if number_2 != 0:  # Check if the second number is not zero
#         print(number_1 / number_2)
#     else:
#         print("Error: Division by zero")
# else:
#     print('Invalid operation sign')




sign = input("please what operation do you want to use?")
digit_1 = float(input("mention your first digit"))
digit_2 = float(input("mention your second digit"))

if sign == "+":
    print(digit_1 + digit_2)
elif sign == "-":
    print(digit_1 - digit_2)
elif sign == "*":
    print (digit_1 * digit_2)
elif sign == "/":
    if digit_2 != 0: 
        print(digit_1 / digit_2)
    else:
        print("error: division by zero")
else: print ('invalid operation sigh')

