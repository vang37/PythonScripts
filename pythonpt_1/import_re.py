# import re
# def compare_strings(string1, string2):
#   #Convert both strings to lowercase 
#   #and remove leading and trailing blanks
#   string1 = string1.lower().strip()
#   string2 = string2.lower().strip()

#   #Ignore punctuation
#   punctuation = r"[.?!,;:\-']"
#   # print("string1: ",  string1, " string2: ",  string2)
#   string1 = re.sub(punctuation, r"", string1)
#   string2 = re.sub(punctuation, r"", string2)

#   #DEBUG CODE GOES HERE
#   # print("string1: ",  string1, " string2: ",  string2)

#   return string1 == string2

# print(compare_strings("Have a Great Day!", "Have a great day?")) # True
# print(compare_strings("It's raining again.", "its raining, again")) # True
# print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three.")) # False
# print(compare_strings("They found some body.", "They found somebody.")) # False

# def linear_search(list, key):
#     """If key is in the list returns its position in the list,
#        otherwise returns -1."""
#     for i, item in enumerate(list):
#         if item == key:
#             return i
#     return -1

# def binary_search(list, key):
#     """Returns the position of key in the list if found, -1 otherwise.

#     List must be sorted.
#     """
#     left = 0
#     right = len(list) - 1
#     while left <= right:
#         middle = (left + right) // 2
        
#         if list[middle] == key:
#             return middle
#         if list[middle] > key:
#             right = middle - 1
#         if list[middle] < key:
#             left = middle + 1
#     return -1

import subprocess, os

folder = os.getcwd()
# print(folder)

# array = os.listdir(folder)
# print(array)

# for root,dirs,files in os.walk(folder):
#   # print("root: ", root, "dirs: ", dirs, "files: ", files) 
#   for f in files:
#     #Extract the sub-folder (if any)
#     path = root[len(folder):]
#     print(root)


# subprocess.call(["ls"]))

# print(array)

#!/usr/bin/env python3

import subprocess, os
from multiprocessing import Pool

folder = os.getcwd()

# def run(task):
#   # source = src + "/" + task
#   print("Handling {}".format(task))
#   # subprocess.call(["rsync", "-arq", task, dest])
# if __name__ == "__main__":
#   # tasks = os.listdir(src)
#   tasks = []
#   for root, dirs, files in os.walk(folder):
#    for name in files:
#       tasks.append(os.path.join(root, name))
#    for name in dirs:
#       tasks.append(os.path.join(root, name))
#   p = Pool(len(tasks))
#   p.map(run, tasks)

tasks = []
for root, dirs, files in os.walk(".", topdown=False):
  #  for name in files:
  #     tasks.append(os.path.join(root, name))
  for name in dirs:
        tasks.append(os.path.join(root, name))

print(tasks)