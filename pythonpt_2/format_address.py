# def format_address(address_string):
#   # Declare variables
#   number = address_string.split()[0]
#   # Separate the address string into parts
#   address_part = address_string.split()[1:]
#   # Traverse through the address parts
#   parts = ""
#   for address in address_part:
#       parts += address + " "
#     # Determine if the address part is the
#     # house number or part of the street name

#   # Does anything else need to be done 
#   # before returning the result?
  
#   # Return the formatted string  
#   return "house number {} on street named {}".format(number, parts)

# print(format_address("123 Main Street"))
# # Should print: "house number 123 on street named Main Street"

# print(format_address("1001 1st Ave"))
# # Should print: "house number 1001 on street named 1st Ave"

# print(format_address("55 North Center Drive"))
# # Should print "house number 55 on street named North Center Drive"

# def highlight_word(sentence, word):
# 	return(sentence.replace(word, word.upper()))

# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))


# def combine_lists(list1, list2):
#   list1_reversed = list1[::-1]
#   # Generate a new list containing the elements of list2
#   # Followed by the elements of list1 in reverse order
#   return(list2 + list1_reversed)
	
# Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
# Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

# print(combine_lists(Jamies_list, Drews_list))

# def combine_guests(guests1, guests2):
#     guests2.update(guests1)
#   # Combine both dictionaries into one, with each key listed 
#   # only once, and the value from guests1 taking precedence
#     return guests2
# Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
# Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

# print(combine_guests(Rorys_guests, Taylors_guests))

def count_letters(text):
  result = {}
  # Go through each letter in the text
  for l in [letter for letter in text if letter.isalpha()]:
    l = l.lower()
    if l not in result:
        result[l] = 0
    result[l] += 1
  return result

# print(count_letters("AaBbCc"))
# # Should be {'a': 2, 'b': 2, 'c': 2}

# print(count_letters("Math is fun! 2+2=4"))
# # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

# print(count_letters("This is a sentence."))
# # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}