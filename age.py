

def age(argY,argM,argD):

    y = argY - 1993
    m = argM - 2
    d = argD - 9

    print y,"years :", m,"months :", d,"days"



print "Set the current date,please >>>"
Y = int(input("\nSet Year:"))
M = int(input("\nSet Month:"))
D = int(input("\nSet Day:"))


print ("\nYour Age now >>> ")
age(Y,M,D)