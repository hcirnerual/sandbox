# Open a file in read mode
with open('filename.txt', 'r') as file:
    content = file.read()

# Open a file in write mode (creates a new file or truncates existing)
with open('filename.txt', 'w') as file:
    file.write("Hello, World!")

# Open a file in append mode (opens for writing at the end)
with open('filename.txt', 'a') as file:
    file.write("This will be appended.")

