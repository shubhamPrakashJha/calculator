print("Simple Python Calculator")
while True:
    print("\nOPTIONS: \nadd for Addition \nsub for Subtraction \nmul for Multiplication \n"
          "div for Division \nquit OR q to Exit \n")
    user_input = input("Give your operation: \n").lower()

    try:
        if ("quit" in user_input) or ("q" in user_input):
            break
        elif "add" in user_input:
            num1 = float(input("enter 1st number"))
            num2 = float(input("enter 2st number"))
            result = str(num1 + num2)
            print(f"Result is {result}\n")
        elif "sub" in user_input:
            num1 = float(input("enter 1st number:\t"))
            num2 = float(input("enter 2st number:\t"))
            result = str(num1 - num2)
            print(f"Result is {result}\n")
        elif "mul" in user_input:
            num1 = float(input("enter 1st number"))
            num2 = float(input("enter 2st number"))
            result = str(num1 * num2)
            print(f"Result is {result}\n")
        elif "div" in user_input:
            num1 = float(input("enter 1st number"))
            num2 = float(input("enter 2st number"))
            result = str(num1 / num2)
            print(f"Result is {result}\n")
        else:
            print("Wrong Input! \n")
    except Exception:
        print("Wrong Input! \n")
        continue
