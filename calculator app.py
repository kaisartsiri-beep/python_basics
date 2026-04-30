while True:
    a=float(input("Enter number: "))
    b=float(input("Enter number: "))
    procedure=input("Enter procedure: ")
    match procedure:
        case "+":
            print(a+b)
        case "-":
            print(a-b)
        case "*":
            print(a*b)
        case "/":
            if b!=0:
                print(a/b)
            else:
                print("Error: Division by zero")

    choice = input("Continue? (y/n): ")
    if choice.lower() == "n":
        print("Goodbye")
        break