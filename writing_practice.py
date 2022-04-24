with open("new_file.txt", "w") as new_file: # Create and open new file
    new_file.write("New content!") # Write to the file

with open("new_file.txt", "r") as new_file # Open the file again, this time in read mode
    contents = new_file.read()

print(contents)