from math import*


class calculator:

    def restart(self):
        option = input("Enter a math symbol. Ex: + - * /    :")

        if option == "+":
            cal.addition(1)
            cal.restart()
        if option == "-":
            cal.subtraction(1)
            cal.restart()
        if option == "*":
            cal.multiplication(1)
            cal.restart()
        if option == "/":
            cal.division(1)
            cal.restart()



    def addition(x,y):
        x = input("Enter a number")
        y = input("Enter another number")
        added = float(x)+float(y)
        print("Your answer is: " + str(added))

    def subtraction(x,y):
        x = input("Enter a number")
        y = input("Enter another number")
        sub = float(x)-float(y)
        print("Your answer is: " + str(sub))

    def multiplication(x,y):
        x = input("Enter a number")
        y = input("Enter another number")
        mult = float(x)*float(y)
        print(mult)

    def division(x,y):
        x = input("Enter a number")
        y = input("Enter another number")
        div = float(x)/float(y)
        print(div)






name=input("Enter your name: ")
ageStr=input("Hello, " + name + " enter your age: ")
age=float(ageStr)

if age<21:
    print("Sorry, " + " but you are not old enough to access the calculator.")
    exit()
else:
    print("You have access to the calculator.")



cal = calculator()
cal.restart()







