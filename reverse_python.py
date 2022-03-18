# def reverse_word(string):
#     reversed_word = []
#     for i in range(len(string) - 1, -1, -1):
#         reversed_word += string[i]
#         return ''.join(reversed_word)

# input_word = input("Enter your word: ")

# print(reverse_word(input_word))

# def reverse_for_loop(s):
#     s1 = ''
#     for c in s:
#         s1 = c + s1  # appending chars in reverse order
#     return s1

# input_str = 'ABç∂EF'

# if __name__ == "__main__":
#     print('Reverse String using for loop =', reverse_for_loop(input_str))


# user_input = input("Please enter your name: ")
# print("hi " + user_input)


x = input("Enter a string: ")

# counter = len(x)

# for z in range(len(x)):
#     print(x[::counter])
#     counter =- 1

y = x[::-1]
print("Reverse of string is: " + y)


# def reverse():
#   z = input("Enter another string: ")
#   for(a = z.length - 1; a<10; a--) {
#     print("Reverse of string is: " + a)
#   }


# formatting print(f"reverse")


# user_input= input("")

# reverse_input = ""

# index = len(user_input) -1

# while(i>=0):
#     reverse_input = reverse_input+ user_input[index]
#     index -= index

# print(reverse_input)