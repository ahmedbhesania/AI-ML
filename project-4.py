print("Data Analyzer and Transformer Program")




#1
def input_data():
    global data
    print("Step 1: Input Data")
    raw = input("Enter data for a list (separated by spaces): ")
    data = [int(x) for x in raw.split()]
    print("Data has been stored successfully")
#2
def display_summary():
    if not data:
        print("No data found. Please input data first")
        return

    
    print("Data Summary:")
    print("- Total elements:", len(data))
    print("- Minimum value:", min(data))
    print("- Maximum value:", max(data))
    print("- Sum of all values:", sum(data))
    print("- Average value:", sum(data) / len(data))
def factorial(n):
    if n == 0 or n == 1:      
        return 1
    else:
        return n * factorial(n - 1)
#3
def factorial_menu():
    n = int(input("Enter a number to calculate its factorial: "))
    if n < 0:
        print("Factorial of negative numbers is not possible.")
    else:
        print(f"Factorial of {n} is:", factorial(n))
#4
def filter_data():
    print("\nStep 4: Filter Data by Threshold (Lambda Function)")
    threshold = int(input("Enter a threshold value to filter data above this value: "))

    filtered = list(filter(lambda x: x > threshold, data))
    print("Filtered Data (values --", threshold, "):")
    print(filtered)
#5
def sort_data():
    print("Choose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        sorted_data = sorted(data)  
        print(sorted_data)
    elif ch == 2:
        sorted_data = sorted(data, reverse=True)
        print(sorted_data)
    else:
        print("Invalid choice!")


#6
def get_statistics():
   
    return min(data), max(data), sum(data) / len(data)


def display_statistics():
    if not data:
        print("No data found. Please input data first!")
        return

    

    minimum, maximum, avg = get_statistics()

  
    print("- Minimum value:", minimum)
    print("- Maximum value:", maximum)
    print("- Sum of all values:", sum(data))
    print("- Average value:", avg)



data = []

while True:
    print("Welcome to the Data Analyzer and Transformer Program")
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = int(input("Please enter your choice: "))

    if choice == 1:
        input_data()
    elif choice == 2:
        display_summary()
    elif choice == 3:
        factorial_menu()
    elif choice == 4:
        filter_data()
    elif choice == 5:
        sort_data()
    elif choice == 6:
        display_statistics()
    elif choice == 7:
        print("Exiting the program... assalamualikum")
        break
    else:
        print("Invalid choice! Please try again.")

