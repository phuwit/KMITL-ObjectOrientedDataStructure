def decode(input_string):
    for char in input_string:
        if input_string.count(char) > 1:
            return ((ord(char) - ord('a')) + 1) * 4

secretCode = input("Enter secret code : ")
print(decode(secretCode))
