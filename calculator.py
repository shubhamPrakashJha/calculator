while True:
    print("OPTIONS:")
    print("add")
    print("sub")
    print("mul")
    print("div")
    print("quit")
    user_input = input(":")

    if user_input == "quit":
        break
    elif user_input =="add":
        num1 = float(input("enter 1st number"))
        num2 = float(input("enter 2st number"))
        result = str(num1 + num2)
        print("result is "+result)
    elif user_input =="sub":
        num1 = float(input("enter 1st number"))
        num2 = float(input("enter 2st number"))
        result = str(num1 - num2)
        print("result is " + result)
    elif user_input =="mul":
        num1 = float(input("enter 1st number"))
        num2 = float(input("enter 2st number"))
        result = str(num1 * num2)
        print("result is " + result)
    elif user_input =="div":
        num1 = float(input("enter 1st number"))
        num2 = float(input("enter 2st number"))
        result = str(num1 / num2)
        print("result is " + result)
    else:
        print("wrong input")

