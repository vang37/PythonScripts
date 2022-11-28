#!/usr/bin/env python3

# import shutil
# import psutil

# def check_disk_usage(disk):
#     du = shutil.disk_usage(disk)
#     free = du.free / du.total * 199
#     return free > 20

# def check_cpu_usage():
#     usage = psutil.cpu_percent(1)
#     return usage < 75

# if not check_disk_usage("/") or not check_cpu_usage():
#     print("ERROR!")
# else:
#     print("Everything is OK!")



# >>> import shutil
# >>> du = shutil.disk_usage("/")
# >>> print(du)
# usage(total=127120965632, used=113252335616, free=13606486016)
# >>> exit()

# (after adding shebang to file)
# MacBook-Pro-3:desktop G_Hughes$ chmod +x int_to_roman.py 
# MacBook-Pro-3:desktop G_Hughes$ ./int_to_roman.py 134
# CXXXIV

# >>> import psutil
# >>> du = psutil.cpu_percent(0.1)
 

# import requests
# import socket

# def check_localhost():
#         localhost = socket.gethostbyname('localhost')
#         print(localhost == "127.0.0.1")
#         return localhost == "127.0.0.1"

# def check_connectivity():
#         request = requests.get("http://www.google.com")
#         print(request.status_code == 200)
#         return request.status_code == 200

# check_localhost()
# check_connectivity()

import os
import datetime

# guests = open("guests.txt", "w")
# initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

# for i in initial_guests:
#     guests.write(i + "\n")
    
# guests.close()

# # with open("guests.txt") as guests:
# #     for line in guests:
# #         print(line)

# new_guests = ["Sam", "Danielle", "Jacob"]

# with open("guests.txt", "a") as guests:
#     for i in new_guests:
#         guests.write(i + "\n")

# guests.close()

# with open("guests.txt") as guests:
#     for line in guests:
#         print(line)

# os.remove("guests.txt")
# print(os.path.exists("guests.txt"))
# print(os.path.getsize("RomanNumerals.docx"))
# print(os.path.getmtime("RomanNumerals.docx"), "<-- Unix timestamp representing number of seconds since January 1st, 1970.")
# timestamp = os.path.getmtime("RomanNumerals.docx")
# print(datetime.datetime.fromtimestamp(timestamp))
# print(os.path.abspath("_"))
# os.mkdir("new_dir")
# os.chdir("new_dir")
# print(os.getcwd())
# os.rmdir("new_dir")

# dir = "website"
# for name in os.listdir(dir):
#     fullname = os.path.join(dir, name)#use os.path.join to join the directory to a file name to create a valid full name (string). 
#     if os.path.isdir(fullname):
#         print("{} is a directory".format(fullname))
#     else:
#         print("{} is a file".format(fullname))


# def new_directory(directory, filename):
#   if os.path.isdir(directory):
#     return "Directory already exists."
#   else:
#     # dir = os.getcwd()
#     os.mkdir(directory)
#     os.chdir(directory)
#     file = open(filename, "w")
#     file.close()
#     os.chdir("..")
#     # os.chdir(dir)
#     files = os.listdir(directory)
#     return files
# print(new_directory("PythonPrograms", "script.py"))

import datetime
import csv


# def file_date(filename):
#   # Create the file in the current directory
#   file = open(filename, "w")
#   timestamp = os.path.getmtime(filename)
#   # Convert the timestamp into a readable format, then into a string
#   date = datetime.datetime.fromtimestamp(timestamp)
#   # print(str(datetime.datetime.fromtimestamp(timestamp))[0:10])
#   # Return just the date portion 
#   # Hint: how many characters are in “yyyy-mm-dd”? 
#   return ("{:.10}".format(str(date)))

# print(file_date("newfile.txt")) 

# hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
# with open("hosts.csv", "w") as hosts_csv:
#     writer = csv.writer(hosts_csv)
#     writer.writerows(hosts)

# with open ("software.csv") as software:
#     reader = csv.DictReader(software)
#     for row in reader: 
#         print(("{} has {} users").format(row["name"], row["users"]))

users = [{"name": "Sol Mansi", "username": "solm", "department": "IT Infrastructure"},
{"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
{"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]#keys to be written to the file
with open ("by_department.csv", "w") as by_department:#open the file for writing
    writer = csv.DictWriter(by_department, fieldnames=keys)# create DictWriter instance, pass it keys 
    writer.writeheader()#creates the first line of the CSV based on keys 
    writer.writerows(users)#turn the list of dictionaries into lines in the CSV file


import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open (filename, "r") as filename:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(filename)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))


import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open (filename. "r") as file:
    # Read the rows of the file
    rows = csv.reader(file)
    # Process each row
    for row in rows:
      name,color,type = row
      # Format the return string for data rows only
      if row[0] != "name" and row[1] != "color" and row[2] != "type":
        return_string += "a {} {} is {}\n".format(row[1], row[0], row[2])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))


employees.csv:
Full Name, Username, Department
Audrey Miller, audrey, Development
Arden Garcia, ardeng, Sales
Bailey Thomas, baileyt, Human Resources
Blake Sousa, sousa, IT infrastructure
Cameron Nguyen, nguyen, Marketing
Charlie Grey, greyc, Development
Chris Black, chrisb, User Experience Research
Courtney Silva, silva, IT infrastructure
Darcy Johnsonn, darcy, IT infrastructure
Elliot Lamb, elliotl, Development
Emery Halls, halls, Sales
Flynn McMillan, flynn, Marketing
Harley Klose, harley, Human Resources
Jean May Coy, jeanm, Vendor operations
Kay Stevens, kstev, Sales
Lio Nelson, lion, User Experience Research
Logan Tillas, tillas, Vendor operations
Micah Lopes, micah, Development
Sol Mansi, solm, IT infrastructure

                                               

#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
        employee_list = []
        for data in employee_file:
                employee_list.append(data)
        return employee_list

employee_list = read_employees(csv_file_location)

# DictReader creates an object that operates like a regular reader
# (an object that iterates over lines in the given CSV file), but
# also maps the information it reads into a dictionary where keys
# are given by the optional fieldnames parameter. If we omit the
# fieldnames parameter, the values in the first row of the CSV file
# will be used as the keys. So, in this case, the first line of the
# CSV file has the keys and so there's no need to pass fieldnames as a parameter.

# We also need to pass a dialect as a parameter to this function.
# There isn't a well-defined standard for comma-separated value files,
# so the parser needs to be flexible. Flexibility here means that there
# are many parameters to control how csv parses or writes data. Rather
# than passing each of these parameters to the reader and writer separately,
# we group them together conveniently into a dialect object.

# Dialect classes can be registered by name so that callers of the CSV module
# don't need to know the parameter settings in advance. We will register a
# dialect empDialect. The main purpose of this dialect is to remove any
# leading spaces while parsing the CSV file.

def process_data(employeeList):
        department_list = []
        for employee_data in employeeList:
                department_list.append(employee_data['Department'])

        department_data = {}
        for department_name in set(department_list):
            department_data[department_name] = department_list.count(department_name)
        return department_data

dictionary = process_data(employee_list)


# This uses the set() method, which converts iterable elements to distinct elements.


def write_report(dict, report_file):
        with open(report_file, "w+") as f:
                for k in sorted(dict):
                        f.write(str(k)+':'+str(dict[k])+'\n')
                f.close()

write_report(dictionary, '')