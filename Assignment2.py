# 1) Convert 1024 to binary and hexadecimal representation
a = 1024
print("The binary number of %d is: " %a, bin(a))
print("The binary number of {} is: ".format(a), hex(a))
print()

# 2) Round 5.23222 to two decimal places
b = 5.23222
print("The round of 5.23222 to two decimal places is: ", round(b, 2))
print()

# 3) Check if every letter in the string s is lower case
s = 'hello how are you Mary, are you feeling okay?'
if s.islower():
    print("All Characters in the string is lower case")
else:
    print("The character of the string is not in lower case")
print()

# 4) How many times does the letter 'w' show up in the string below?
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print("Count of 'w' in %s is : "%s,s.count('w'))
print()

# 5) Reverse the list
list1 = [1,2,3,4]
print("The reverse of the list {} is: " .format(list1), list1[::-1])
print(list1)
# Alternate method. After reverse method list order gets changed permanently
list1.reverse()
print("The reverse of the list [1,2,3,4] is: ", list1)
print(list1)
print()


# 6) Sort the list
list2 = [3,4,2,5,1]
list2.sort()
print("The sort of the list [3,4,2,5,1] is: ", list2)
print(list2)  # After sorting the list order gets changed permanently
print()

# 7) Based on rules, Write a program that picks a random integer from 1 to 100, and has players guess the number.
import random
num = random.randint(1, 100)
#print(num) #Displays the secret number number
print("GUESS ME!")
print("There's a guessed number between 1 and 100")
print("If your guess is within 10 of the guessed number, I'll display you're WARM")
print("If your guess is more than 10 away from the guessed number, I'll display you're COLD")
print("If your guess is closer than your most recent guess, I'll display you're WARMER")
print("If your guess is farther than your most recent guess, I'll display you're COLDER")
print("Let's Play!")

guesses = [0]  # Created list to store the guesses
while True:     # loop until correct:
    guess = abs(int(input("Enter a number that you guess between 1 to 100: ")))
    if guess < 1 or guess > 100:
        print('Out of Bounds! Please Try Again')
        continue
    if guess == num:
        print("WON! You've guessed the number in %d guesses" % (len(guesses)))
        break
    guesses.append(guess)  # Adding current guess to the list

    if guesses[-2]:     # After appending all new guesses to the list, then the previous guess is given as guesses[-2]
        if abs(num-guess) < abs(num-guesses[-2]):   # checks current guess diff < prev guess diff
            print("Warmer: You are closer now than before")
        else:
            print("Colder: You are farther away now than before")
    else:
        if num-guess <= 10:
            print('WARM!')
        else:
            print('COLD!')
