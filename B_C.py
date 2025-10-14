
print ("NOTE :\nIf you anytime want to quit from the calculator, press 'Q' during the operation selection.\n")

while True:
    try:
        A = float(input("Enter the first number: "))
        B = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
   
    print("If you want to perform an operation you have to put the symbols of the operation\nFor addition it is +\nFor subtraction it is -\nFor multiplication it is x\nFor division it is /\nFor modulus it is %\nFor exponent it is ^")

    op = input ("Enter the operation you want to perform : ")
    if(op == "Q"):
        print ("You have successfully quit the calculator operation")
        break
    match op:
        case "+":
            print(A+B)
        case "-":
            print(A-B)
        case "/":
            if B == 0:
                print("Cannot divide by zero.")
            else:
                print(A / B)
        case "x":
            print(A * B)
        case "^":
            print(A**B)
        case "%":
            print(A%B)
        case _:
            print("An Error !")
