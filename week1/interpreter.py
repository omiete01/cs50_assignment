# assignment week 1
# this a calculator that takes in users expression and calculates the result 

expression = input("Expression: ")

x, y, z = expression.split(" ")
x = float(x)
z = float(z)

if y == "+":
    result = x+z
    print(result)
elif y == "-":
    result = x-z
    print(result)
elif y == "/":
    result = x/z
    print(round(result, 2))
elif y == "*":
    result = x*z
    print(result)

# print(x,y,z)