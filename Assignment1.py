# 1) Value of the expressions
a = 4 * (6+5)
print('The value of the expression 4 * (6 + 5) is: ', a)
b = 4 * 6 + 5
print('The value of the expression 4 * 6 + 5 is: ', b)
c = 4 + 6 * 5
print('The value of expression 4 + 6 * 5 is: ', c)

# Alternative Method
a = 4 * (6+5)
b = 4 * 6 + 5
c = 4 + 6 * 5
print('The value of expressions of a, b, c is: ', a,b,c)

# 2) Print out 'e' from 'hello' using indexing
s = 'hello'
print('The index value of 1 is : ', s[1])

# 3) Equation to print 100.25 using operators
Eqn = 100/2 + (5 ** 2)*2 + 0.50 - 0.25
print('The result of equation is : ', Eqn)

# 4) Reverse the string 'hello' using slicing
print('The reverse string of hello is : ', s[::-1])

# 5) Given the string hello, give two methods of producing the letter 'o' using indexing
# Method 1
print("First method to display letter 'o': ", s[-1])
print("Second method to display letter 'o': ", s[4])

# 6) Question based on Booleans
a = 2 > 3
print('The result of 2 > 3 is : ', a)
b = 3 <= 2
print('The result of 3 <= 2 is : ', b)
c = 3 == 2.0
print('The result of 3 == 2.0 is : ', c)
d = 3.0 == 3
print('The result of 3.0 == 3 is : ', d)

# 7) Print only the words that start with s in this sentence using split()
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)

# 8) Displays stars(*) in right angled triangular
rows = abs(int(input('Enter the total number of rows :')))
print(f'Star Pattern Right Angled Triangular with {rows} rows : ')
for i in range(rows):
    for j in range(i+1):
        print('*', end= '')
    print()

# 9) Display even numbers between m and n accept the values through input for m and n
m = int(input('Enter the starting Number: '))
n = int(input('Enter the Ending Number: '))
if n <= m:
    print(f'Enter the value which is greater than start number {m}')
    n = int(input('Enter the Ending Number: '))
else:
    pass
for num in range(m, n + 1):
    if num % 2 == 0:
        print(num, end= ' ')
    else:
        pass
print()

# 10) printing each letter on a separate line, except backwards.
str = 'fruit'
index = len(str) - 1
print('The letter of the string fruit is :')
while index >= 0:
    letter = str[index]
    print(letter)
    index = index - 1

