#intro

import time

print("Hello! Welcome to your basic interactive calculator!")
time.sleep(2)
print("I will be computing basic calculations for you.")
time.sleep(2)
print("Are you ready to start?")
time.sleep(2)
start = str(input("Please type Yes if ready: "))
start

while start != "Yes" and start != "yes":
    print("I'm sorry, I don't understand.")
    time.sleep(2)
    print("You are still welcome to type Yes at any time.")
    time.sleep(2)
    start = str(input("Please type Yes if ready: "))
    start
else:
    print("Fantastic! Let's get started.")


#basic calculation

time.sleep(2)
print("To start, let's do a simple 4-function calculation.")
time.sleep(2)
print("I'm going to have you enter two integers, and I will compute the sum, difference, product, and quotient.")
time.sleep(4)

number1= float(input("Enter the first number: "))
number2= float(input("Enter the second number: "))

firstsum = (number1 + number2)
firstdifference = (number1 - number2)
firstproduct = (number1*number2)
firstquotient = (number1/number2)

print("The sum of your two numbers =", firstsum)
time.sleep(2)
print("The difference of your two numbers =", firstdifference)
time.sleep(2)
print("The product of your two numbers =", firstproduct)
time.sleep(2)
print("The quotient of your two numbers =", firstquotient)
time.sleep(2)

#further calculations

print("Great! You have completed the introductory calculations.")
time.sleep(2)
print("Now, I am going to leave everything in your hands.")
time.sleep(2)
print("Are you ready to begin?")
time.sleep(2)
print("Please type Yes if ready.")
time.sleep(2)

independent = str(input("Your Answer: "))
independent

while independent != "Yes" and independent != "yes":
    print("I'm sorry, I don't understand.")
    time.sleep(2)
    print("You are still welcome to type Yes at any time.")
    time.sleep(2)
    independent = str(input("Your Answer: "))
    independent
else:
    print("Fantastic! Let's get started.")


#independent calculations

time.sleep(2)
print("To start, please enter the number of the operation you would like to use first: ")
time.sleep(2)
print("1. Addition")
time.sleep(1)
print("2. Subtraction")
time.sleep(1)
print("3. Multiplication")
time.sleep(1)
print("4. Division")
time.sleep(1)

while 1==1:
    function1 = int(input("Number of Operation: "))
    function1
    if function1 != 1 and function1 != 2 and function1 != 3 and function1 != 4:
        print("I'm sorry, I don't understand.")
        time.sleep(2)
        print("Please type the number corresponding to the operation you would like to use (1-4).")
        time.sleep(2)
    elif function1 == 1:
        print("You have chosen addition.")
        time.sleep(1)
        print("Enter any two numbers")
        time.sleep(1)
        number3= float(input("1. "))
        number4= float(input("2. "))
        number3
        number4
        sumfunction1= number3 + number4
        print(sumfunction1)
    elif function1 == 2:
        print("You have chosen subtraction.")
        time.sleep(1)
        print("Enter any two numbers")
        time.sleep(1)
        number5= float(input("1. "))
        number6= float(input("2. "))
        number5
        number6
        subtractionfunction1= (number5 - number6)
        print(subtractionfunction1)
    elif function1 == 3:
        print("You have chosen multiplication.")
        time.sleep(1)
        print("Enter any two numbers")
        time.sleep(1)
        number7= float(input("1. "))
        number8= float(input("2. "))
        number7
        number8
        multiplicationfunction1= (number7 * number8)
        print(multiplicationfunction1)
    else:
        print("You have chosen division.")
        time.sleep(1)
        print("Enter any two numbers")
        time.sleep(1)
        number9= float(input("1. "))
        number10= float(input("2. "))
        number9
        number10
        divisionfunction1= (number9 / number10)
        print(divisionfunction1)
