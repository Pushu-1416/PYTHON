# Easy:  Write a program to print the sum of the digits in the number.  
# Testcase1 : 101  
# Output : 2  
# Explanation : Sum of the digits in the number 1+0+1 = 2, Answer is 2.  
# Testcase1 : 567  
# Output : 18  
# Explanation : Sum of the digits in the number 5+6+7 = 18, Answer is  18.  


# a=int(input("enter a number: "))
# sum=0
# while a>0:
#     b=a%10
#     sum=sum+b
#     a=a//10
# print(sum)


# Write a program to print reverse of the given number.  
# Testcase1 : 721  
# Output : 127  
# Explanation : Reverse of the number 721 is 127.  
# Testcase1 : 765  
# Output : 567  
# Explanation : Reverse of the number 765 is 567.


# a=int(input("enter a number: "))
# b = 0
# while a > 0:
#     d=a % 10
#     b=b * 10 + d
#     a=a//10
# print(b)

  
# Write a program to print factorial of the number.  
# Testcase1 : 3  
# Output : 6  
# Explanation : Factorial of the number 3 is 3*2*1 = 6.  
# Testcase1 : 4  
# Output : 24  
# Explanation : Factorial of the number 4 is 4*3*2*1 = 24.
 
 
# a=int(input("enter a number: "))
# fact=1
# for i in range(1, a + 1):
#     fact = fact * i
# print(fact) 

 
#  Write a program to print middle character(s) in the given string or 
# number.  
# Testcase1 : Wonder  
# Output : nd  
# Explanation : The middle characters in the given word Wonder is nd.  
# Testcase1 : World  
# Output : r  
# Explanation : The middle character in the given word World is r.  Test Case 1 : 6969  
# Output : 96  
# Explanation : The middle character in the given number 6969 is 96.


# a = input("Enter a string or number: ")
# n = len(a)
# if n % 2 == 0:
#     print(a[n//2-1:n//2+1])
# else:
#     print(a[n//2])
 
 
  
#  Write a program to check whether the sum of digits in the number except  
# first digit and digit is equal to the sum of first digit and last digit of that  number. If both the sums are equal then print equal otherwise print not  equal  
# Testcase1 : 75547  
# Output : equal  
# Explanation : In the given number 7557, first digit and last digit sum  that is sum(7,7)=14 is equal to sum of remaining numbers that is  sum(5,5,4) = 14. So both sums are equal.  
# Testcase1 : 765  
# Output : not equal  
# Explanation : Sum(7,5)=12 and Sum(6)=6, both sums are not equal. 


# a = input("Enter a number: ")
# first = int(a[0])
# last = int(a[-1])
# middle_sum = 0
# for i in a[1:-1]:
#     middle_sum += int(i)
# if first + last == middle_sum:
#     print("equal")
# else:
#     print("not equal") 
 

 
#  Write a program to check whether the digits in-between the first and last  
# digit are less than first and last digit, if yes then print true, otherwise print  false.  
# Testcase1 : 1672  
# Output : false
# Explanation : The middle digits 6,7 are not less than first digit 1 and  last digit 7 .  
# Testcase1 : 84719  
# Output : true  
# Explanation : The middle digits 4,7,1 are less than first digit 8 and last  digit 9 .  


# a = input("Enter a number: ")
# first = int(a[0])
# last = int(a[-1])
# flag = True
# for i in a[1:-1]:
#     if int(i) >= first or int(i) >= last:
#         flag = False
#         break
# if flag:
#     print("true")
# else:
#     print("false")



#  Write a program to print the vowels in the given string in reverse order.  
# Testcase1 : Helloworld  
# Output : ooe  
# Explanation : Vowels in the given string Helloworld are e,o,o . The  reverse order of eoo is ooe.  
# Testcase1 : JackspArrow  
# Output : oAa  
# Explanation : Vowels in the given string JackspArrow are a,A,o . The  reverse order of aAo is oAa. 


# a = input("Enter a string: ")
# vowels = ""
# for i in a:
#     if i in "aeiouAEIOU":
#         vowels += i
# print(vowels[::-1])
 
 
 
#  Write a program to print the vowels in the given string and repeated  vowel should be printed only single time.  
# Testcase1 : Helloworld  
# Output : eo  
# Explanation : Vowels in the given string Helloworld are e,o,o . The  single vowels among them are eo .  
# Testcase1 : Jacksparrow  
# Output : ao  
# Explanation : Vowels in the given string Helloworld are a,a,o . Among  them a is repeated more than once, so consider it for one time , result is  ao.


# a = input("Enter a string: ")
# result = ""
# for i in a:
#     if i in "aeiouAEIOU" and i not in result:
#         result += i
# print(result)



#  Write a program to print the string after removing the duplicate characters  in the string.  
# Testcase1 : madam  
# Output : d  
# Explanation : In the given string madam, the duplicates are m,a. After  removing m’s and a’s from the given string we formed a new string d.  
# Testcase1 : donkey  
# Output : donkey  
# Explanation : In the given string there is no duplicate character. 


# a = input("Enter a string: ")
# result = ""
# for i in a:
#     if a.count(i) == 1:
#         result += i
# print(result)
 
 
 
#  Write a program to convert all the upper case letters in the given string to  lower case letter and vice versa.  
# Testcase1 : JohnWick  
# Output : jOHNwICK  
# Explanation : All the upper case letters changed to lower case and vise  versa.  
# Testcase1 : Korean  
# Output : kOREAN  
# Explanation : All the upper case letters changed to lower case and vise  versa.


# a = input("Enter a string: ")
# result = ""
# for i in a:
#     if i.isupper():
#         result += i.lower()
#     elif i.islower():
#         result += i.upper()
#     else:
#         result += i
# print(result)
 
 
  
#  Write a program to print all the Upper case letters in the string in reverse  order and then followed by the lower case letters .  
# Testcase1 : NumberOne  
# Output : ONumberne  
# Explanation : In the given string NumberOne, Uppercase letters are N,O.  The reverse order of them are ON next it is followed by lowe case letters  (umberne). So final string is ONumberne.
# Testcase1 : ClassLeader  
# Output : LClasseader  
# Explanation : In the given string ClassLeader, Uppercase letters are C,L.  The reverse order of them are LC next it is followed by lowe case letters  (lasseader). So final string is LClasseader. 


# a = input("Enter a string: ")
# upper = ""
# lower = ""
# for i in a:
#     if i.isupper():
#         upper += i
#     elif i.islower():
#         lower += i
# print(upper[::-1] + lower)



# Array-Based Questions :
# Find the Largest Element in an Array 
# Problem: Write a function to return the largest number in an array. 
# Testcase 1: 
# Input: [3, 1, 4, 1, 5, 9] 
# Output: 9 
# Explanation: 
# In the array [3, 1, 4, 1, 5, 9], the largest number is 9. 


# arr = list(map(int, input("Enter elements: ").split()))
# largest = arr[0]
# for i in arr:
#     if i > largest:
#         largest = i
# print("Largest element:", largest)


#  Find the Second Largest Element 
# Problem: Write a function to return the second largest number in an array. 
# Testcase 1: 
# Input: [3, 1, 4, 1, 5, 9] 
# Output: 5 
# Explanation: 
# In the array [3, 1, 4, 1, 5, 9], the second largest number after 9 is 5. 
#  Sum of All Elements 


# arr = list(map(int, input("Enter elements: ").split()))
# largest = second = float('-inf')
# for i in arr:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second and i != largest:
#         second = i
# print("Second largest element:", second)



# Problem: Write a function that returns the sum of all elements in an array. 
# Testcase 1: 
# Input: [1, 2, 3, 4] 
# Output: 10
# Explanation: 
# The sum of the elements 1 + 2 + 3 + 4 = 10. 
#  Remove Duplicates from an Array 


# arr = list(map(int, input("Enter elements: ").split()))
# total = 0
# for i in arr:
#     total += i
# print("Sum:", total)


# Problem: Write a function to remove duplicate values from an array. 
# Testcase 1: 
# Input: [1, 2, 2, 3, 4, 4, 5] 
# Output: [1, 2, 3, 4, 5] 
# Explanation: 
# The duplicates 2 and 4 are removed from the array, leaving [1, 2, 3,  4, 5]. 
#  Check if Array is Sorted
 

# arr = list(map(int, input("Enter elements: ").split()))
# result = []
# for i in arr:
#     if i not in result:
#         result.append(i)
# print(result)


# Problem: Write a function to check if an array is sorted in ascending  order.  
# Testcase 1: 
# Input: [1, 2, 3, 4, 5] 
# Output: true 
# Explanation: 
# The array [1, 2, 3, 4, 5] is sorted in ascending order. 
#  Reverse an Array 


# arr = list(map(int, input("Enter elements: ").split()))
# flag = True
# for i in range(len(arr)-1):
#     if arr[i] > arr[i+1]:
#         flag = False
#         break
# if flag:
#     print("true")
# else:
#     print("false")



# Problem: Write a function to reverse the elements in an array. 
# Testcase 1: 
# Input: [1, 2, 3, 4, 5] 
# Output: [5, 4, 3, 2, 1] 
# Explanation: 
# The array [1, 2, 3, 4, 5] is reversed to [5, 4, 3, 2, 1].
#  Remove Falsy Values 


# arr = list(map(int, input("Enter elements: ").split()))
# reverse = []
# for i in range(len(arr)-1, -1, -1):
#     reverse.append(arr[i])
# print(reverse)


# Problem: Write a function that removes all falsy values from an array.  Falsy values include false, 0, "", null, undefined, and NaN. 
# Testcase 1: 
# Input: [0, 1, false, 2, '', 3] 
# Output: [1, 2, 3] 
# Explanation: 
# The falsy values 0, false, and "" are removed from the array, leaving  [1, 2, 3]. 
#  Find Unique Elements 


# arr = input("Enter elements separated by space: ").split()
# result = []
# for i in arr:
#     if i not in ['0', 'False', 'false', '', 'None', 'none', 'NaN', 'nan']:
#         result.append(i)
# print(result)


# Problem: Write a function to find the unique elements in an array  (elements that appear only once). 
# Testcase 1: 
# Input: [1, 2, 2, 3, 4, 4, 5] 
# Output: [1, 3, 5] 
# Explanation: 
# The unique elements that appear only once in the array are 1, 3, and 5. 
#  Sum of Even Numbers 


# arr = list(map(int, input("Enter elements: ").split()))
# result = []
# for i in arr:
#     if arr.count(i) == 1:
#         result.append(i)
# print(result)



# Problem: Write a function that returns the sum of all even numbers in an  array. 
# Testcase 1: 
# Input: [1, 2, 3, 4, 5] 
# Output: 6 
# Explanation:
# The even numbers in the array are 2 and 4. Their sum is 2  

# arr = list(map(int, input("Enter elements: ").split()))
# sum = 0
# for i in arr:
#     if i % 2 == 0:
#         sum += i
# print(sum)


#  String-Based Questions
# Reverse a String : 
# Question: Write a function to reverse a given string.
# Testcase: "hello"
# Output: "olleh"
# Explanation: The reverse of the string "hello" is "olleh". Each character's order is reversed.

# def reverse_string(s):
#     return s[::-1]
# text = "hello"
# print(reverse_string(text))


# Check if a String is a Palindrome
# Question: Write a function to check if a given string is a palindrome.
# Testcase: "racecar"
# Output: true
# Explanation: A palindrome is a string that reads the same forward and backward. Since "racecar" is the same in both directions, the output is true.


# def is_palindrome(s):
#     return s == s[::-1]
# text = "racecar"
# print(is_palindrome(text))


# Count Vowels in a String
# Question: Write a function to count the number of vowels in a given string.
# Testcase: "hello world"
# Output: 3
# Explanation: The vowels in "hello world" are 'e', 'o', and 'o'. Thus, the total count of vowels is 3.


# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for ch in s:
#         if ch in vowels:
#             count += 1
#     return count
# text = "hello world"
# print(count_vowels(text))


# Remove Vowels from a String
# Question: Write a function to remove all vowels from a given string.
# Testcase: "hello world"
# Output: "hll wrld"
# Explanation: After removing the vowels 'e', 'o', and 'o' from "hello world", we are left with "hll wrld".

# def remove_vowels(s):
#     vowels = "aeiouAEIOU"
#     result = ""
#     for ch in s:
#         if ch not in vowels:
#             result += ch
#     return result
# text = "hello world"
# print(remove_vowels(text))

# Convert String to Title Case
# Question: Write a function that converts a string to title case (capitalize the first letter of each word).
# Testcase: "hello world"
# Output: "Hello World"
# Explanation: The first letter of each word is capitalized, resulting in "Hello World".


# def title_case(s):
#     return s.title()
# text = "hello world"
# print(title_case(text))


# Convert String to Number
# Question: Write a function to convert a string to a number (without using parseInt or Number).
# Testcase: "123"
# Output: 123
# Explanation: The string "123" is converted to the number 123.


# def string_to_number(s):
#     num = 0
#     for ch in s:
#         digit = ord(ch) - ord('0')
#         num = num * 10 + digit
#     return num
# text = "123"
# print(string_to_number(text))


# Check if String Contains Only Digits
# Question: Write a function to check if a string contains only numeric digits.
# Testcase: "12345"
# Output: true
# Explanation: The string "12345" consists only of digits, so the result is true.


# def only_digits(s):
#     for ch in s:
#         if ch < '0' or ch > '9':
#             return False
#     return True
# text = "12345"
# print(only_digits(text))


# Count Occurrences of a Character
# Question: Write a function that counts the occurrences of a specific character in a string.
# Testcase: "hello world", "l"
# Output: 3
# Explanation: The character 'l' appears 3 times in the string "hello world".


# def count_character(s, ch):
#     count = 0
#     for i in s:
#         if i == ch:
#             count += 1
#     return count
# text = "hello world"
# character = "l"
# print(count_character(text, character))


# Object-Based Questions
# Convert Array to Object
# Question: Write a function that converts an array of key-value pairs into an object.
# Testcase: [["name", "Alice"], ["age", 25]]
# Output: {name: "Alice", age: 25}
# Explanation: The key-value pairs in the array are converted into properties of an object. "name" maps to "Alice", and "age" maps to 25.


# def array_to_object(arr):
#     result = {}
#     for key, value in arr:
#         result[key] = value
#     return result
# data = [["name", "Alice"], ["age", 25]]
# print(array_to_object(data))


# Merge Two Objects
# Question: Write a function that merges two objects, giving priority to the properties of the second object in case of conflict.
# Testcase: {a: 1, b: 2}, {b: 3, c: 4}
# Output: {a: 1, b: 3, c: 4}
# Explanation: The property b in the second object overrides the property b in the first object, resulting in {a: 1, b: 3, c: 4}.


# def merge_objects(obj1, obj2):
#     result = obj1.copy()
#     for key, value in obj2.items():
#         result[key] = value
#     return result
# obj1 = {"a": 1, "b": 2}
# obj2 = {"b": 3, "c": 4}
# print(merge_objects(obj1, obj2))


# Count Object Properties
# Question: Write a function that returns the number of properties in an object.
# Testcase: {a: 1, b: 2, c: 3}
# Output: 3
# Explanation: The object {a: 1, b: 2, c: 3} has 3 properties, so the output is 3.
# Get Object Keys


# def count_properties(obj):
#     count = 0
#     for key in obj:
#         count += 1
#     return count
# obj = {"a": 1, "b": 2, "c": 3}
# print(count_properties(obj))


# Question: Write a function that returns an array of all the keys in an object.
# Testcase: {a: 1, b: 2, c: 3}
# Output: ["a", "b", "c"]
# Explanation: The keys of the object are "a", "b", and "c", so the function returns an array of these keys.

# def get_keys(obj):
#     keys = []
#     for key in obj:
#         keys.append(key)
#     return keys
# obj = {"a": 1, "b": 2, "c": 3}
# print(get_keys(obj))


# Get Object Values
# Question: Write a function that returns an array of all the values in an object.
# Testcase: {a: 1, b: 2, c: 3}
# Output: [1, 2, 3]
# Explanation: The values of the object are 1, 2, and 3, so the function returns an array of these values.


# def get_values(obj):
#     values = []
#     for value in obj.values():
#         values.append(value)
#     return values
# obj = {"a": 1, "b": 2, "c": 3}
# print(get_values(obj))


# Check if Object is Empty
# Question: Write a function to check if an object is empty (i.e., has no properties).
# Testcase: {}
# Output: true
# Explanation: Since the object has no properties, the function returns true.


# def is_empty(obj):
#     if len(obj) == 0:
#         return True
#     else:
#         return False
# obj = {}
# print(is_empty(obj))

