'''Write a program that prints the number of characters in a user's name.
 You might need to Google for a function that calculates the length of a string.
'''
value = input('Enter your string here \n')
print(len(value))

# Write a program that switches the values stored in the variables a and b. 
#Take the input in one line
a,b = map(int, input('Enter a and b with space separated \n').split(' '))
b,a = a,b
print(a,b)

# Band Generator program
print('Hello ! Welcome to band name generator! 1\n')
city = input('Enter your city\n')
pet = input('Enter your pet\'s name \n')
band_name = city+" "+pet
print('your brand name is !! {} \n',band_name)