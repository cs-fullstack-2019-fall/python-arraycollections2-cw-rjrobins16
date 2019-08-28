# Python review CW
# Problem 1:
# Create code and define the variable below outside of any function.
# After you create the list variable write a function called ```stupid_array_tricks```
# that takes an array as a parameter, and performs the functions listed below in the instructions.
person_array = ["Kenn", "Kevin", "Erin", "Autumn"]
# a) Print the 2nd and 3rd elements of the person_array using a *range*
print (person_array[1:3])  # prints second and third element from list
# b) Print the last 2 elements of the person_array using a *range*
print (person_array[2:4])
# c) Insert the new element ```Chuck``` between the 2nd (```Kevin```) and 3rd (```Erin```) elements
person_array.insert(2, "Chuck")
print (person_array)
# d) Take out the 2nd element (```Kevin```) from the list
person_array.pop(1)
print (person_array)

# Problem 2:
# We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.
userInput = ""
while userInput != "q":
    userInput = input("Enter a word or q to quit.")

# Problem 3:
# Create a function that uses the data list below.
data = ['GOOD_DATA', 'DECENT_DATA', 'BAD_DATA', 'DECENT_DATA', 'GOOD_DATA', 'BAD_DATA', 'GOOD_DATA', 'DECENT_DATA',
        'BAD_DATA', 'GOOD_DATA']
# Write the code to do the following:
# * Print the length of the original DATA list/array (ex. ```Starting length of data list is 10```)
print(len(data))
# * Remove all ```BAD_DATA``` from the DATA list/array
for x in data:
    if x == 'BAD_DATA':
        data.pop()
print (data)
# * Print the length of the final DATA list/array (ex. ```Ending length of data list is 7```)
# !! Print the length of the final DATA list/array

# Problem 4:
# Use the following list of 5 numbers.
score_list = [21, 14, 6, 8, 28, 42, 21]
# Write the code to do the following:
# * Print the sum of the numbers (ex. ```The SUM of the numbers is 140 ```)
print (f'The sum of the numbers is {(sum(score_list))}')
# * Print the maximum value from the numbers (ex. ```The MAX of the numbers is 140 ```)
print(f'The max value of the numbers is {(max(score_list))}')
# * Print the minimum value from the numbers (ex. ```The MIN value of the numbers is 6 ```)
print(f'The min value of the numbers is {(min(score_list))}')
# Challenge:
# Create a program that will let the User build a list words. Prompt the User for a word. Add the word the User enters and add it to the list. Allow the User to keep entering words until they enter 'x' to exit the program.
#
# Print the final word list prior to exiting the program.
