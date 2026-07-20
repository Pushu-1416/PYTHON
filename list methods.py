# Basic Level
# Create a list of 5 integers and print it.
# a=[1,2,3,10,14]
# print(a)


# Write a program to find the length of a list without using len().
# c=1
# a=[1,2,3,'anjali']
# for i in a:
#     c=c+1
# print(c)


# Access and print the last element of a list.
# a=[1,2,3,'anjali']
# a=a[3]
# print(a)


# Add an element to the end of a list.
# a=[1,2,3,4]
# a.append('anjali')
# print(a)


# Insert an element at the 2nd position in a list.
# a=[1,2,3,4]
# a.insert(2,'anjali')
# print(a)


#  Intermediate Level
# Remove a specific element from a list.
# a=[1,2,3,4,'anjali']
# a.pop(4)
# print(a)


# Remove the element at index 3.
# a=[18,7,4,45,8,77]
# a.pop(3)
# print(a)


# Count how many times a specific element appears in a list.
# a=[1,2,3,4,4,4,5,6,7,7]
# a=a.count(4)
# print(a)


# Sort a list in ascending and descending order.
# a=[9,8,3,4,6,7]
# a.sort()
# a.sort(reverse=True)
# print(a)


# Reverse a list without using reverse() method.
# a=[9,8,7,6,5,4,3,2,1]
# a=a[::-1]
# print(a)


# Find the maximum and minimum number in a list (without using max() and min()).
# Merge two lists into one.
# a=[1,2,3,4]
# b=[5,6,7,8]
# c=a+b
# print(c)


# Remove duplicate elements from a list.
# a=[1,2,3,3,4,5,6,6]
# result = []
# for i in a:
#     if i not in result:
#         result.append(i)
# print(result)


# Find the sum of all elements in a list (without using sum()).
# a = [1, 2, 3, 4, 5]
# total = 0
# for i in a:
#     total += i
# print(total)


# Create a list of even numbers between 1 and 50 using list comprehension.
# even = [i for i in range(1, 51) if i % 2 == 0]
# print(even)


#  Advanced Level
# Rotate a list to the right by k positions.
# a = [1, 2, 3, 4, 5]
# k = 2
# k = k % len(a)
# result = a[-k:] + a[:-k]
# print(result)


# Find the second largest number in a list.
# a = [10, 20, 5, 40, 30]
# largest = second = float('-inf')
# for i in a:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second and i != largest:
#         second = i
# print(second)


# Check if a list is a palindrome.
# a = [1, 2, 3, 2, 1]
# if a == a[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# Flatten a nested list (e.g., [[1,2],[3,4],[5]]).
# nested = [[1, 2], [3, 4], [5]]
# flat = []
# for sublist in nested:
#     for item in sublist:
#         flat.append(item)
# print(flat)


# Find the frequency of each element in a list and store it in a dictionary.
# a = [1, 2, 2, 3, 3, 3, 4]
# freq = {}
# for i in a:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
# print(freq)
