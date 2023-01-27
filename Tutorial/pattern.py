"""
n = int(input("Enter the no of rows"))

x = bool(input("Press 1 for print normally of 0 for upside down"))

if(x == 1):

    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end=' ')
            print()
if(x == 0):
    """
for i in range(5, 1):
    for j in range(1, i+1):
        print("*", end=' ')
        print()
