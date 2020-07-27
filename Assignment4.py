# 1) Write code to create Queue using List and provide all the functionalities of the Queue
# Initializing a queue using list
queue = []

# Add an element to the back of the queue (known as enqueuing)
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Remove an element from the front of the queue (known as dequeuing).
print("\nElements removed from queue in FIFO behaviour")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

# Check to see if the queue is empty.
print("\nQueue after removing elements")
print(queue)
print()

# 2) Write code to create Stack using List and provide all the functionalities of the Stack

# Stack creation.
stack = []

# Add an element to the top of the stack (known as pushing onto the stack)
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# Remove an element from the top of the stack (known as popping from the stack)
# LIFO order
print('\nElements removed from stack in LIFO behaviour')
print(stack.pop())
print(stack.pop())
print(stack.pop())

# Check to see if the stack is empty.
print('\nStack after elements are removed:')
print(stack)
print()

# 3) Create two sets of students, one for those who took an exam and one for those that submitted a project.
# simple strings is used to represent the students
# Set up sets
# exam = {'Andrew', 'Kirsty', 'Beth', 'Emily', 'Sue'}
# project = {'Kirsty', 'Emily', 'Ian', 'Stuart'}
# Using these sets write the code using different set methods to show the below following question functionalities:
# • Which students took both the exam and submitted a project?
# • Which students only took the exam?
# • Which students only submitted the project?
# • List all students who took either (or both) of the exam and the project.
# • List all students who took either (but not both) of the exam and the project.

exam = {'Andrew', 'Kirsty', 'Beth', 'Emily', 'Sue'}
project = {'Kirsty', 'Emily', 'Ian', 'Stuart'}

print(f"The students belongs to exam = {exam} and project = {project}")
print("The students took both the exam and submitted a project : \n", exam.intersection(project))
print("The students only took the exam : \n", exam.difference(project))
print("The students only submitted the project : \n", project.difference(exam))
print("The students who took either (or both) of the exam and the project : \n", exam.union(project))
print("The students who took either (but not both) of the exam and the project : \n", exam.symmetric_difference(project))
print()

# 4) A program to calculate prime number starting from 1 up to the value input by the user
num = int(input("Enter the number to print between its prime values : "))
if num > 1:
    for val in range(2, num):
        for i in range(2, val):
            if val % i == 0:  # if the value is divisible by any of the num itself then it's not prime
                break
        else:
            print(val)
else:
    print("Error Occurs")
    num = int(input("Enter the number greater than 2 to print all its prime values : "))
print()

# 5) Find the elements in set1 that are not in set2:
# Find all elements that are in either set:
# set1 = {2,3,1,5,6,8}
# set2 = {3,1,7,5,6,8}

set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}
print(f"The elements in {set1} that are not in {set2} is : ", set1.symmetric_difference(set2))
print(f"The elements that are in either set  {set1} and {set2} is : ", set1.union(set2))
print()

# 6) Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension

dict = {num: num**3 for num in range(4)}
print("Expected dictionary using dictionary comprehension is : ", dict)
print()

# 7) Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

for fizzbuzz in range(1, 100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
print()

# 8) Checks if the string entered by the user is a palindrome for “racecar”

string = input("Enter the string to check for palindrome or not : ")
tmp = list(string.lower())      # Converted string to a list in the form of lower case & stored in a tmp variable
reversed_string = list(string[::-1])    # Converted reverse of the string in the list &  stored in another variable
if tmp == reversed_string:  # Comparing the original string with the reverse of the entered string
    print(f"The entered string {string} is a palindrome.")
else:
    print(f"The entered string {string} is not a Palindrome.")
print()