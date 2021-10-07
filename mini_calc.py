def add(a, b):
   return a + b

def subtract(a,b):
    return a - b

def divide(a, b):
    return a / b

first_int = int(input("what's the first number? : "))
sign = input("sign")
second_int = int(input("whats the second number? : "))

# print(first_int)
if sign == "+" :
    answer = add(first_int, second_int)
    print(answer)
elif sign == "-" :
    answer = subtract(first_int, second_int)
    print(answer)
else:
    answer = divide(first_int, second_int)
    print(answer)

