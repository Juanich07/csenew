# 6. Object-Oriented Programming (OOP)
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

# Instantiate objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Call methods
print(f"{dog1.name} says {dog1.bark()}")
print(f"{dog2.name} says {dog2.bark()}")

# 7. Exception Handling
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print(f"An error occurred: {e}")

# 8. File Handling
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample file.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 9. Version Control
# Set up a version control system (git commands)
# Initialize a repository
# Add files
# Commit changes
# Push changes to a remote repository

# 10. Debugging
# Introduce intentional bugs and use debugging tools to identify and fix them12