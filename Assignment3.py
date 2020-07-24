# 1) [Arise But It Juliet Who already and breaks east envious fair grief is kill light moon pale sick soft sun the through what window
# with yonder]
# Write a program to read all the lines or entire data in the object, and split into a list of words .
# For each word, check to see if the word is already in a list.
# If the word is not in the list, add it to the list, so at the end we need to get the list which has all unique words only
# When the program completes, sort and print the resulting words in alphabetical order.

str = "Arise But It Juliet Who already and breaks east envious fair grief is kill light moon pale sick soft sun the through what window with yonder"
lst = list()
word = str.split()
for element in word:
    if element not in lst:      
        lst.append(element)
print('The resulting words in alphabetical order is: \n', sorted(lst))
print()

# 2) Using the same data provided in Problem1 ,create a dictonary , perform the same operation like splitting the line in to words
# and check each word , if it is not present then add to the dictionary , if it is present then increment the count of the
# word added. Then sort the dictonary and display the words So at the end the dictionary ,should be sorted and should have key as the word and the value as the count of the words

string = "Arise But It Juliet Who already and breaks east envious fair grief is kill light moon pale sick soft sun the through what window with yonder"
counts = dict()
words = string.split()
for word in words:
    if word not in counts:      # It checks whether the word is not present in dictionary
        counts[word] = 1        # If the word(i.e key) is not present in dictionary then count is assigned to 1
    else:
        counts[word] += 1       # counts get incremented
print('The result of the sorted dictionary holds the key as the word and the value as the count of the words is: \n', counts)
print()

# 3) For the specified string , retrive time and display separately

line = "stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
nline = line.split()
l = nline[4]
new = l.split()
new = new[0]
print(f'For the specified string, {line} \n The result of retrieving time and display separately is : ', new)
print()

# 4) Write a program to read different values from the user and convert all the values received in to list and then compute average of all the values and display the output
lst = []
sum = 0
total = int(input("How many numbers you want to print? :"))
for t in range(0, total):
    num = int(input("Enter the number: "))
    lst.append(num)     # adding the element
print("The entered numbers in List is : ", lst)
for iterate in lst:
    sum = sum + iterate
    avg = sum/len(lst)
print("The Average of the List %s is : %.2f" % (lst, avg))
print()


# 5) Write a program to read through mail rececipt and retrive Day of the week and Month of the year
# then display as dictonary which will have Day of week as key and its value as month of the year
# You can decide on the value data type
# for e.g the output should be {'Sat':'Jan','Mar'}
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# From stephen.marquard@uct.ac.za Fri Feb 5 09:14:16 2008
# From stephen.marquard@uct.ac.za Sat Mar 5 09:14:16 2008
# From stephen.marquard@uct.ac.za Fri Feb 5 09:14:16 2008
# From stephen.marquard@uct.ac.za Mon Jan 5 09:14:16 2008
# From stephen.marquard@uct.ac.za Tue Apr 5 09:14:16 2008

mail_receipt = ['From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008',
                'From stephen.marquard@uct.ac.za Fri Feb 5 09:14:16 2008',
                'From stephen.marquard@uct.ac.za Sat Mar 5 09:14:16 2008',
                'From stephen.marquard@uct.ac.za Fri Feb 5 09:14:16 2008',
                'From stephen.marquard@uct.ac.za Mon Jan 5 09:14:16 2008',
                'From stephen.marquard@uct.ac.za Tue Apr 5 09:14:16 2008']
dict = {}
list = []
for read_mail in mail_receipt:
    list = read_mail.split()
    if list[2] in dict:
        dict[list[2]] = [list[2], list[3]]
    else:
        dict[list[2]] = list[3]
print('The resulted dictionary holds the Day of week as key and its value as month of the year like : \n', dict)
print()

# 6) Write program to receive the input of temperature in celsius and convert it into fahrenheit

value = float(input("Enter the temperature in Celsius: "))
res = (value * 9/5) + 32    # celsius * 1.8 = fahrenheit - 32 #general formula
print("Entered temperature %.2f in Celsius is converted to %.2f in Fahrenheit "%(value, res))
print()

# 7) Write a program to prompt from the user for a score between 0.0 and 1.0.
# If the score is out of range print an error. If the score is between 0.0 and 1.0,
# print a grade using the following table

while True:
    score = abs(float(input("Enter your score between 0.0 to 1.0:")))
    if score < 0.0 or score > 1.0:
        print("The score is out of range. Enter the score valid between 0.0 to 1.0")
        continue
    elif score >= 0.9:
        print(f"The Grade of your score {score} is A")
    elif score >= 0.8:
        print(f"The Grade of your score {score} is B")
    elif score >= 0.7:
        print(f"The Grade of your score {score} is c")
    elif score >= 0.6:
        print(f"The Grade of your score {score} is D")
    else:
        print(f"The Grade of your score {score} is F")
    break
print()

# 8) Find the largest value in a list [3, 41, 12, 9, 74, 15], construct the program using either for loop or while loop

lst = [3, 41, 12, 9, 74, 15]
tmp = lst[0]
for num in lst:
    if num > tmp:
        tmp = num
print("The largest value in a list %s is : " % lst, tmp)



