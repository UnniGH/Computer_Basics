fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

name = "Python"
for char in name:
    print(char)

for i in range(5): 
    print(i)

count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# While loop with a break statement
num = 1
while True:
    print("Number is:", num)
    if num == 3:
        break  # Exits the loop when num is 3
    num += 1

# Simulating a do-while loop for user input validation
while True:
    user_input = input("Enter a positive number: ")
    if user_input.isdigit() and int(user_input) > 0:
        number = int(user_input)
        print(f"You entered: {number}")
        break  # Exit the loop if input is valid
    else:
        print("Invalid input. Please enter a positive integer.")