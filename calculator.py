# Calculato
from calculatorArt import logo
def add(n1, n2):
    """it add up"""
    return n1 + n2
def subtract(n1, n2):
    """it subtract two inputs"""
    return n1 - n2
def multiply(n1, n2):
    """ it multiplies functions"""
    return n1 * n2
def divide(n1, n2):
    """it divides functions"""
    return n1 / n2
def modulus(n1, n2):
    """ it retuens remaider after division"""
    return n1 % n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulus,

}

def calculator():
    print(logo)
    num1 = float(input("what's the first number?: "))
    for operators in operation:
        print(operators)
    continueIt = True
    while continueIt:

        operation_symbbol = input("Pick an operation from the line above: ")
        num2 = float(input("Whats the second number: "))
        calculationFunction = operation[operation_symbbol]
        answer = calculationFunction(num1, num2)

        print(f"{num1} {operation_symbbol} {num2} = {answer}")

        if input(f"do you want to continue the calculation with {answer} type 'y' to continue and 'n' to start a new calculation: \n") == "y":
            num1 = answer
        else:
            #this right here is called recusion because we are calling a function inside itsellf. if this is done without a valid condition the code will become an infite loop so there should always be a codition before calling a function iside itself.
            calculator()
calculator()

    

