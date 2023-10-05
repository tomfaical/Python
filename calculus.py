# simple equation function; takes a value for x and the equation for y and returns y
def simpleEquation(x, expression):
    expression = list(expression)
    for i in range(len(expression)):
        if expression[i] == "x":
            expression[i] = f"{x}"
    expression = "".join(expression)
    y = eval(expression)
    return y


# you have to write ALL operators, in python lingo
print(simpleEquation(3, "x**2+360*x"))
