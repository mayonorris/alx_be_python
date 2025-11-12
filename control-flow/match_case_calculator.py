# Simple Calculator with Match Case

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /)): ")

match operation:
    case "+":
        result = first_num + second_num
    case "-":
          result = first_num - second_num
    case "*":
        result = first_num * second_num
    case "/":
        if second_num == 0:
            print("Cannot divide by zero.")
        else:
            result = first_num/second_num
    case _:
        print("This is not a supported operation")
print(f"The result is {result}.")

