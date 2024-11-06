n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    x=int(input("Enter numbers: ")) 
    numbers.append(x)
print(numbers)
while True:
    print("\nMenu:")
    print("1. Find the greatest and lowest number")
    print("2. Sort the list in ascending order")
    print("3. Create a list of even numbers")
    print("4. Exit")
 
    choice = input("Enter your choice (1-4): ")
 
    if choice == '1':
        print("Greatest number:", max(numbers))
        print("Lowest number:", min(numbers))
 
    elif choice == '2':
        print("Sorted list:", sorted(numbers))
 
    elif choice == '3':
        even_numbers = []
        for num in numbers:
            if num % 2 == 0:
                even_numbers.append(num)
        print("List of even numbers:", even_numbers)
 
    elif choice == '4':
        print("Exiting the program.")
        break
 
    else:
        print("Invalid choice. Please choose a number from 1 to 4.")
