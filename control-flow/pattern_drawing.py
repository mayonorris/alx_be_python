# Drawing Patterns with Nested Loops: This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).

size = int(input("Enter the size of the pattern: "))
i = 1
while i <= size:
    for _ in range(1, size + 1):
        print("*", end = "")
    print()
    i += 1
