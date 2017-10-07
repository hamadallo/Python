# a program to check if a value odd or ever.

def checkOdd(arg):
    #global arg
    if arg % 2 == 0:
        return "Even"
    else:
        return "Odd"

x = int(input("Enter a number: "))
print "The number ",x , " is ",checkOdd(x)
