# File Creation
with open('my_file.txt', 'w') as file:
    file.write("Hello, this is Onesmas Kiratu.\n")
    file.write("I am a teacher: I have taught for 15 years.\n")
    file.write("I would like to master the Python programming language.\n")


# File Reading and Display
with open('my_file.txt', 'r') as file:
    content = file.read()
    print(content)

# File Appending
with open('my_file.txt', 'a') as file:
    file.write("Hello, this is David Njenga.\n")
    file.write("I am a Software Developer: I have worked for 10 years.\n")
    file.write("I would like to be a full-stack developer.\n")

# Error Handling
try:
    # File Creation
    with open('my_file.txt', 'w') as file:
        file.write("Hello, this is Onesmas Kiratu.\n")
        file.write("I am a teacher: I have taught for 15 years.\n")
        file.write("I would like to master the Python programming language.\n")


# File Reading and Display
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print(content)

# File Appending
    with open('my_file.txt', 'a') as file:
        file.write("Hello, this is David Njenga.\n")
        file.write("I am a Software Developer: I have worked for 10 years.\n")
        file.write("I would like to be a full-stack developer.\n")
  
# My own addition
# File Reading and Display Again to confirm append
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("\nContent of the file after appending:")
        print(content)
        
except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("You do not have permission to access or modify the file.")
finally:
    print("Operation complete.")
