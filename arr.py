# Function to create and print array

def create_array():
    arr = []

    n = int(input("Enter number of elements: "))

    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)

    print("\nArray elements are:")
    for item in arr:
        print(item)

# Function call
create_array()