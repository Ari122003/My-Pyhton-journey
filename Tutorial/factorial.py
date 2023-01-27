
def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac*(i+1)


x = int(input("Enter number\n"))
factorial_iterative(x)
