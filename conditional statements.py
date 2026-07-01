#CONDITIONAL STATEMENTS:
#Check whether a number is positive, negative, or zero.
#Determine if a number is even or odd.
#Check if a person is eligible to vote (age ≥ 18).
#Find the largest of two numbers.
#Find the largest of three numbers.
#Check whether a year is a leap year.
#Determine if a character is a vowel or consonant.
#Check whether a number is divisible by 5 and 11.
#Assign grades based on marks (A, B, C, D, Fail).
#Check if a number is a multiple of both 3 and 7.
#Determine whether a given number is a two-digit number.
#Check if a character is an alphabet, digit, or special character.
#Create a simple calculator using if-elif (add, subtract, multiply, divide).
#Check whether a triangle is valid based on its angles.
#Determine the type of triangle (equilateral, isosceles, scalene).
#Find whether a number is greater than 100, equal to 100, or less than 100.
#Check if a given temperature is cold, warm, or hot.
#Determine whether a person is a child, teenager, adult, or senior based on age.
#Check whether a number lies between 1 and 50.
#Verify if a given password is valid (length condition).
#Check if a year is a century year.
#Determine whether a number is divisible by 2, 3, or both.
#Find the smallest of three numbers.
#Check whether a number is a perfect square (basic logic).
#Determine the profit or loss based on cost price and selling price.
#Check if a student passes or fails (minimum marks condition).
#Determine whether a given day number (1–7) is a weekday or weekend.
#Check if a number is positive and even.
#Classify BMI into underweight, normal, overweight, obese.
#Determine electricity bill category based on units consumed.


#a=int(input("enter a number: "))
#if a>0:
#    print("positive")
#elif a<0:
#    print("negative")
#else:
#    print("zero")


#a=int(input("enter a number: "))
#if a % 2 == 0:
#   print("even")
#else:
#    print("odd")


#a=int(input("enter age: "))
#if a>=18:
#    print("eligible to vote")
#else:
#    print("not eligible")


#a=int(input("enter a number: "))
#b=int(input("enter a number: "))
#if a>b:
#    print("a is largest")
#else:
#     print("b is largest")


#a=int(input("enter a number: "))
#b=int(input("enter a number: "))
#c=int(input("enter a number: "))
#if a >= b and a >= c:
#    print("a is largest")
#elif b >= a and b >= c:
#    print("b is largest")
#else:
#    print("c is largest")


#a=int(input("enter a year: "))
#if (a % 400 == 0 or a % 4 == 0) and (a %100 != 0):
#    print("leap year")
#else:
#    print("non leap")


#a=input("enter a character: ")
#if a in "aeiouAEIOU":
#    print("vowel")
#else:
#    print("consonant")


#a=int(input("enter a number: "))
#if a % 5 == 0 and a % 11 == 0:
#    print("divisible by 5 and 11")
#else:
#    print("not divisible by 5 and 11")


#a=int(input("enter marks: "))
#if a >= 75:
#    print("A grade")
#elif a >= 65:
#    print("B grade")
#elif a >= 55:
#    print("C grade")
#elif a >= 45:
#    print("D grade")
#else:
#    print("fail")


#a=int(input("enter a number: "))
#if a%3==0 and a%7==0:
#    print("multiple of 3 and 7")
#else:
#    print("not a multiple of 3 and 7")


#a=int(input("enter a number: "))
#if a >= 10 and a <= 99:
#    print("two digit number")
#else:
#    print("not a two digit number")


#a=input("enter character: ")
#if (a >= 'A' and a <= 'Z') or (a >='a' and a <= 'z'):
#    print("it is a character")
#elif a >= '0' and a <= '9':
#    print("it is a number")
#else:
#    print("special character")


#a= float(input("Enter first number: "))
#b= float(input("Enter second number: "))
#print("1. Addition")
#print("2. Subtraction")
#print("3. Multiplication")
#print("4. Division")
#choice = int(input("Enter your choice : "))

#if choice == 1:
#    print(a + b)
#elif choice == 2:
#    print(a - b)
#elif choice == 3:
#    print(a * b)
#elif choice == 4:
#    if b!= 0:
#        print(a / b)
#else:
#    print("Invalid choice")


#a=int(input("enter first angle: "))
#b=int(input("enter second angle: "))
#c=int(input("enter third angle: "))
#if a > 0 and b > 0 and c > 0 and (a + b + c == 180):
#    print("triangle")
#else:
#    print("not a triangle")


#a=int(input("enter first angle: "))
#b=int(input("enter second angle: "))
#c=int(input("enter third angle: "))
#if a==b and b==c:
#    print("equilateral triangle")
#elif a==b or b==c or c==a:
#    print("isosceles")
#elif a!=b or b!=c or c!=a:
#    print("scalene")


#a=int(input("enter a number :"))
#if a>100:
#    print("greater than 100")
#elif a<100:
#    print("less than 100")
#else:
#    print("equal to 100")


#a=int(input("enter temperature: "))
#if a>40:
#    print("hot")
#elif a>=20 and a<40:
#    print("warm")
#else:
#    print("cold")

#a=int(input("enter age: "))
#if a>0 and a<12:
#    print("adult")
#elif a>13 and a<19:
#    print("teenager")
#elif a>20 and a<59:
#    print("adult")
#else:
#    print("senior")


#a=int(input("enter a number: "))
#if a>1 and a<50:
#    print("lies between 1 and 50")
#else:
#    print("not lies between")


#a=int(input("enter a year: "))
#if a % 100==0:
#    print("centuary year")
#else:
#    print("non centuary year")


#a=int(input("enter a number: "))
#if a % 2 == 0 and a % 3 == 0:
#    print("divisible by both 2 and 3")
#elif a % 2 == 0:
#    print("divisible by 2")
#elif a % 3 == 0:
#    print("divisible by 3")


#a=int(input("enter a number: "))
#b=int(input("enter a number: "))
#c=int(input("enter a number: "))
#if a <= b and a <= c:
#    print("a is smallest")
#elif b <= a and b <= c:
#    print("b is smallest")
#else:
#    print("c is smallest")


#a=float(input("enter sp: "))
#b=float(input("enter cp: "))
#if a>b:
#    print("profit")
#elif a<b:
#    print("loss")
#else:
#    print("no profit no loss")


#a=int(input("enter marks: "))
#if a>=45:
#    print("pass")
#else:
#    print("fail")


#a=int(input("enter a number: "))
#if a > 0 and a % 2 == 0:
#    print("positive and even")
#else:
#    print("negative and odd")


#a=int(input("enter age: "))
#if a > 0 and a < 40:
#    print("under weight")
#elif a>40 and a<70:
#    ptint("normal weight")
#elif a>70 and a<100:
#    print("over weight")
#else:
#    print("obses")






