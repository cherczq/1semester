a = int(input(":"))
b = int(input(":"))
try:
    c = a / b
except (ZeroDivisionError) as error:
    print(error)
finally:
    print("print always")