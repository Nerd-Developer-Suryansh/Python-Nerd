# Ask the user how many elements they want to input
n = int(input("Enter the number of elements: "))

# Initialize an empty list
user_list = []

# Collect the user inputs and append them to the list
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    user_list.append(element)

# Print the final list
print("User-defined list:", user_list)
