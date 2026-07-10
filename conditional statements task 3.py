#If you want to practice conditional statements (if, elif, else) in Python, here are problems from easy to challenging.
#Basic Level
#Positive, Negative, or Zero
#Input a number.
#Print whether it is positive, negative, or zero.
#Even or Odd
#Input an integer.
#Print whether it is even or odd.
#Eligible to Vote
#Input a person's age.
#If the age is 18 or above, print "Eligible to vote", otherwise print "Not eligible".
#Greatest of Two Numbers
#Input two numbers.
#Print the greater number.
#Greatest of Three Numbers
#Input three numbers.
#Print the greatest one.

#Intermediate Level
#Leap Year Checker
#Input a year.
#Print whether it is a leap year.
#Grade Calculator
#Input marks (0–100).
#Display the grade:
#90–100 → A
#80–89 → B
#70–79 → C
#60–69 → D
#Below 60 → F
#Character Type
#Input a single character.
#Print whether it is:
#Uppercase letter
#Lowercase letter
#Digit
#Special character
#Largest Among Four Numbers
#Input four numbers.
#Print the largest.
#Divisibility Check
#Input a number.
#Check if it is divisible by both 3 and 5.


#If you want to practice conditional statements (if, elif, else) in Python, here are problems from easy to challenging.
#Basic Level
#Positive, Negative, or Zero
#Input a number.
#Print whether it is positive, negative, or zero.
#Even or Odd
#Input an integer.
#Print whether it is even or odd.
#Eligible to Vote
#Input a person's age.
#If the age is 18 or above, print "Eligible to vote", otherwise print "Not eligible".
#Greatest of Two Numbers
#Input two numbers.
#Print the greater number.
#Greatest of Three Numbers
#Input three numbers.
#Print the greatest one.

#Intermediate Level
#Leap Year Checker
#Input a year.
#Print whether it is a leap year.
#Grade Calculator
#Input marks (0–100).
#Display the grade:
#90–100 → A
#80–89 → B
#70–79 → C
#60–69 → D
#Below 60 → F
#Character Type
#Input a single character.
#Print whether it is:
#Uppercase letter
#Lowercase letter
#Digit
#Special character
#Largest Among Four Numbers
#Input four numbers.
#Print the largest.
#Divisibility Check
#Input a number.
#Check if it is divisible by both 3 and 5.
#Advanced Level
#Calculator
#Input two numbers and an operator (+, -, *, /).
#Perform the operation using if-elif-else.
#Triangle Validity
#Input three angles.
#Check whether they can form a triangle.
#Triangle Type
#Input three sides.
#Print whether the triangle is:
#Equilateral
#Isosceles
#Scalene
#BMI Category
#Input weight (kg) and height (m).
#Calculate BMI and print:
#Underweight
#Normal
#Overweight
#Obese
#Electricity Bill
#Input units consumed.
#Calculate the bill:
#First 100 units → ₹5/unit
#Next 100 units → ₹7/unit
#Above 200 units → ₹10/unit

#Challenge Problems
#Find the Smallest of Three Numbers
#Check Whether a Character is a Vowel or Consonant
#Check Whether a Number is a 2-Digit, 3-Digit, or More
#Admission Eligibility
#A student is eligible if:
#Marks ≥ 60
#Attendance ≥ 75%
#Print whether the student is eligible.
#Discount Calculator
#Input purchase amount.
#Apply discount:
#Above ₹5000 → 20%
#₹2000–₹5000 → 10%
#Below ₹2000 → No discount
#These questions use only conditional statements (if, elif, else) and basic input/output, making them ideal for mastering decision-making in Python before moving on to loops and functions.




#a=int(input("enter a number: "))
#if a>0:
#    print("positive")
#elif a<0: 
#    print("negative")
#else:
#    print("zero")


#a=int(input("enter a number: "))
#if a % 2 == 0:
#    print("even number")
#else:
#    print("odd")

#a=int(input("enter your age: "))
#if a >= 18:
#    print("eligible to vote")
#else:
#    print("not eligible")


#a=int(input("enter a number: "))
#b=int(input("enter a nyumber: "))
#if a > b:
#    print("a is greater")
#else:
#    print("b is greater")

#a=int(input("enter a number: "))
#b=int(input("enter a number: "))
#c=int(input("enter a number: "))
#if a > b and a > c:
#    print("a is greater")
#elif b > a and b > c:
#    print("b is greater")
#else:
#    print("c is greater")


#a=int(input("enter a year: "))
#if a % 4 == 0 and a % 100 != 0:
#    print("leap year")
#else:
#    print("non leap")


#a=int(input("enter marks: "))
#if a > 90 and a < 100:
#    print("A grade")
#elif a>80 and a<89:
#    print("B grade")
#elif a>70 and a<79:
#    print("C grade")
#elif a>60 and a<69:
#    print("D grade")
#else:
#    print("Fail")


#a=input("enter a character")
#if 'A'<= a <= 'z':
#    print("upper case")
#elif 'a'<= a <= 'z':
#    print("Lower case")
#elif '0' <= a <= '9':
#    print("Number")
#else:
#    print("special character") 


#a=int(input("enter a number: "))
#b=int(input("enter a number: "))
#c=int(input("enter a number: "))
#d=int(input("enter a number: "))
#if a>b and a>c and a>d:
#    print("a is greater")
#elif b>a and b>c and b>d:
#    print("b is greater")
#elif c>a and c>b and c>d:
#    print("c is greater")
#else:
#    print("d is greater")


#a=int(input("enter a number: "))
#if a % 3 == 0 and a % 5 == 0:
#    print("divisible by both 3 and 5")
#else:
#    print("not divisible")


#a=int(input("enter a number: "))
#b=int(input("enter a number: "))
#c=input("enter operator: ")
#if c == "+":
#    print(a+b)
#elif c=="-":
#    print(a-b)
#elif c=="*":
#    print(a*b)
#elif c=="%":
#    print(a%b)
#else:
#    print("invalid number")


#a=int(input("enter a number: "))
#b=int(input("enter a number: "))
#c=int(input("enter a number: "))
#if a > 0 and b > 0 and c > 0 and (a+b+c==180):
#    print("it is a triangle")
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


#a=int(input("enter a number: "))
#b=int(input("enter a number: "))
#c=int(input("enter a number: "))
#if a < b and a < c:
#    print("a is greater")
#elif b < a and b < c:
#    print("b is greater")
#else:
#    print("c is greater")


#a=input("enter a character: ")
#if a in "aeiouAEIOU":
#    print("vowel")
#else:
#    print("consonant")


#a=int(input("enter a number: "))
#if a >= 10 and a <= 99:
#    print("two digit number")
#elif a >= 100 and a <= 999:
#   print("three digit number")
#elif a>=1000:
#    print("more number")
#else:
#    print("not a two digit or three digit number")


#a=int(input("enter marks: "))
#b=int(input("enter attendance: "))
#if a >= 60 and b >= 75:
#    print("eligible")
#else:
#    print("not eligible")


#a=float(input("enter mount: "))
#if a >= 5000:
#    discount=a/100*20
#    a=a-discount
#    print(a)
#elif a>=2000:
#    discount=a/100*10
#    a=a-discount
#    print(a)
#else:
#    print(a)















    
