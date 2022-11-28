# for left in range(7):
#     for right in range (left, 7):
#         print("["+ str(left) + "|" + str(right) + "]", end=" ")
#     print()
    
# def is_palindrome(input_string):
#     # input_string = input_string.strip().lower()
#     new_string = ""
#     reverse_string = ""
#     for i in range(len(input_string)):
#         if input_string[i] != " ":
#             new_string = new_string + input_string[i].lower()
#             reverse_string = input_string[i].lower() + reverse_string
#     if new_string == reverse_string:
#         return True
#     return False


# print(is_palindrome("Never Odd or Even"))
# print(is_palindrome("abc"))
# print(is_palindrome("kayak"))

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames = []

for filename in filenames:
    if filename.find(".hpp") > 0:
        newfilename = filename[:-2]
    else:
        newfilename = filename
    newfilenames.append((filename, newfilename))
print(newfilenames) 