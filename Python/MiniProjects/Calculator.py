def calc(a,b,op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
    
a = int(input("Enter 1st Number :"))
b = int(input("Enter 2nd Number : "))
op = input("Enter Operator (+ - * /)")
print(f"The answer is {calc(a,b,op)}")
