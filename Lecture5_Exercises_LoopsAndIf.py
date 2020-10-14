# modify the code so that the evens list contains only the even
#numbers of the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    if number%2 == 0:
     evens.append(number)


# Add a clause to the if statement such that if the user
#input is "q", your program print "Quit"
user_input = input("Enter your choice: ")
if user_input == "a":
    print("Add")
elif user_input == "q":
    print("Quit")