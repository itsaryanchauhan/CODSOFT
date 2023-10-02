num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation of choice(*,/,+,-): ")
while operation  not in ( "*" , "+" , "-" , "/"):
    print("Error! Choose one of the given operations only")
    operation = input("Enter operation of choice(*,/,+,-): ")
if operation == "*":
    answer = num1*num2
elif (operation) == "/":
        answer = num1/num2
elif (operation) == "+":
          answer = num1+num2
elif (operation) == "-":
           answer = num1-num2

print(answer)
