a = float(input("Please give the value of a (it may not be zero): "))


if a == 0:
    print("There is an error, 'a' cannot be zero.")
else:
    b = float(input("Please give the value of b: "))
    c = float(input("Please give the value of c: "))

    # Solves the equation for x using the formula x = (c - b) / a
    x = (c - b) / a

    print(f"The value of x is: {x}")