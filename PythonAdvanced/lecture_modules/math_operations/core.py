mapper = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "^": lambda x, y: x ** y,

}

def calculate(num1, num2, sign):
    function = mapper[sign]
    return function(num1, num2)