def inp_num(num):
    while True:
        try:
            return float(input(f"Enter number {num}: "))
        except ValueError as v:
            print("Invalid input, please enter a number")


while True:
    num1=inp_num(1)
    num2=inp_num(2)
    sign=input("Enter operation that you want to perform: ")
    if sign == "+":
        result=num1+num2
        break
    elif sign == "-":
        result = num1-num2
        break
    elif sign == "/":
        if num2!=0:
            result = num1/num2
            break
        else:
            print("Division by zero")
            continue
    elif sign == "*":
        result = num1*num2
        break
    elif sign == "**":
        result=num1**num2
        break
    elif sign == "%":
        result=num1%num2
        break
    else:
        print("Invalid operation type, try again")
        
print(f"The output of calculation {num1}{sign}{num2} =",result)
