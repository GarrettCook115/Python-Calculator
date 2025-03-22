
print("calculator")
num1 = float(input("enter your first number"))
num2 = float(input("enter your second number"))

op = int(input("Select an operation ""\n"
      "1 - add""\n"
      "2 - subt""\n"
      "3 - div""\n"
      "4 - multip""\n"))

if op == 1:
    print("added equals:",num1 + num2)
if op == 2:
    print("subtracted equals:",num1 - num2)
if op == 3:
    print("divided equals:",num1 / num2)
if op == 4:
    print("multiplied equals:",num1 * num2)