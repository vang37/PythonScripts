# import os
# import subprocess

# my_env = os.environ.copy()
# print(my_env["PATH"])

# my_env["PATH"] = os.pathsep.join(["/opt/myapp/"f, my_env["PATH"]])

# result = subprocess.run(["myapp"], env=my_env)
# import os
# import re
# import sys

# logfile = sys.argv[1]
# usernames = {}
# with open(logfile) as f:
#     for line in f:
#         if "CRON" not in line:
#             continue
#         pattern = r"USER \((\w+)\)$"
#         result = re.search(pattern, line)
#         if result is None:
#             continue
#         name = result[1]
#         usernames[name] = usernames.get(name, 0) + 1
# print(usernames)


# And now, we'll set the value associated with the key as one more than the current value,
# and we'll use the get method to get the current value, like this.

# Again, we're taking the current value in the dictionary by passing a default value
# of zero, so that when the key is in present in the dictionary, we had a default value.
# We then add one and set it as a new value associated with that key.


# line = "Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"
# pattern = r"\[(\d+)\]"
# result = re.search(pattern, line)
# print(str(line[:15]) + "pid:"+ str(result[1]))


#!/usr/bin/env python3


# def error_search(log_file):
#   error = input("What is the error? ")
#   returned_errors = []
#   with open(log_file, mode='r', encoding='UTF-8') as file:
#     for log in file.readlines():
#       error_patterns = ["error"]
#       for i in range(len(error.split(' '))):
#         error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
#       if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
#         returned_errors.append(log)
#     file.close()
#   return returned_errors

# def file_output(returned_errors):
#   with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
#     for error in returned_errors:
#       file.write(error)
#     file.close()
# if __name__ == "__main__":
#   log_file=sys.argv[1]
#   returned_errors=error_search(log_file)
#   file_output(returned_errors)
#   sys.exit(0)

# import re

# def rearrange_name(name):
#     result = re.search(r"^([\w .]*), ([\w .]*)$", name)
#     if result is None:
#         return name
#     return "{} {}".format(result[2], result[1])

# def character_frequency(filename):

#     try:
#         f = open(filename)
#     except OSError:
#         return None

#     characters = {}
#     for line in f:
#         for char in line:
#                 characters[char] = characters.get(char, 0) + 1
#     f.close()
#     return characters

# def validate_user(username, minlen):
#     assert type(username) == str, "username must be a string"
#     if minlen < 1:
#         raise ValueError("minlen must be at least 1")
#     if len(username) < minlen:
#         return False
#     if not username.isalnum():
#         return False
#     return True

# # print(validate_user(["name"], 1))

# #!/usr/bin/env python3

# import csv
# import sys


# def populate_dictionary(filename):
#   """Populate a dictionary with name/email pairs for easy lookup."""
#   email_dict = {}
#   with open(filename) as csvfile:
#     lines = csv.reader(csvfile, delimiter = ',')
#     for row in lines:
#       name = str(row[0].lower())
#       email_dict[name] = row[1]
#   return email_dict

# def find_email(argv):
#   """ Return an email address based on the username given."""
#   # Create the username based on the command line input.
#   try:
#     fullname = str(argv[1] + " " + argv[2])
#     # Preprocess the data
#     email_dict = populate_dictionary('/home/{{ username }}/data/user_emails.csv')
#      # If email exists, print it
#     if email_dict.get(fullname.lower()):
#       return email_dict.get(fullname.lower())
#     else:
#       return "No email address found"
#   except IndexError:
#     return "Missing parameters"

# def main():
#   print(find_email(sys.argv))

# if __name__ == "__main__":
#   main()


# #!/usr/bin/env python3

# import unittest
# from emails import find_email


# class EmailsTest(unittest.TestCase):
#   def test_basic(self):
#     testcase = [None, "Bree", "Campbell"]
#     expected = "breee@abc.edu"
#     self.assertEqual(find_email(testcase), expected)

#   def test_one_name(self):
#     testcase = [None, "John"]
#     expected = "Missing parameters"
#     self.assertEqual(find_email(testcase), expected)

#   def test_two_name(self):
#     testcase = [None, "Roy","Cooper"]
#     expected = "No email address found"
#     self.assertEqual(find_email(testcase), expected)

# if __name__ == '__main__':
#   unittest.main()

#!/usr/bin/env python3

# import sys
# import subprocess

# with open(sys.argv[1], "r") as f:
#     string_array = f.readlines() 
#     for string in string_array:
#         string = string.strip()
#         subprocess.run(["mv", string, string.replace("jane", "jdoe")])

# import re
# line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
# result = re.search(r"ticky: INFO: ([\w ]*) ", line)
# print(result)

