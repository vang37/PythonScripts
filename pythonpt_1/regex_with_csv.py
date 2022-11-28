# user_emails.csv

# Full Name, Email Address
# Blossom Gill, blossom@abc.edu
# Hayes Delgado, nonummy@utnisia.com
# Petra Jones, ac@abc.edu
# Oleg Noel, noel@liberomauris.ca
# Ahmed Miller, ahmed.miller@nequenonquam.co.uk
# Macaulay Douglas, mdouglas@abc.edu
# Aurora Grant, enim.non@abc.edu
# Madison Mcintosh, mcintosh@nisiaenean.net
# Montana Powell, montanap@semmagna.org
# Rogan Robinson, rr.robinson@abc.edu
# Simon Rivera, sri@abc.edu
# Benedict Pacheco, bpacheco@abc.edu
# Maisie Hendrix, mai.hendrix@abc.edu
# Xaviera Gould, xlg@utnisia.net
# Oren Rollins, oren@semmagna.com
# Flavia Santiago, flavia@utnisia.net
# Jackson Owens, jackowens@abc.edu
# Britanni Humphrey, britanni@ut.net
# Kirk Nixon, kirknixon@abc.edu
# Bree Campbell, breee@utnisia.net
# student-02-21656fe22197@linux-instance:~/data$ cd ~/scripts
# student-02-21656fe22197@linux-instance:~/scripts$ ls
# script.py
# student-02-21656fe22197@linux-instance:~/scripts$ sudo chmod 777 script.py

# student-02-21656fe22197@linux-instance:~/scripts$ nano script.py
# student-02-21656fe22197@linux-instance:~/scripts$ ./script.py
# student-02-21656fe22197@linux-instance:~/scripts$ ls ~/data
# updated_user_emails.csv  user_emails.csv
# student-02-21656fe22197@linux-instance:~/scripts$ cat ~/data/updated_user_emails.csv
# Full Name, Email Address
# Blossom Gill, blossom@xyz.edu
# Hayes Delgado, nonummy@utnisia.com
# Petra Jones, ac@xyz.edu
# Oleg Noel, noel@liberomauris.ca
# Ahmed Miller, ahmed.miller@nequenonquam.co.uk
# Macaulay Douglas, mdouglas@xyz.edu
# Aurora Grant, enim.non@xyz.edu
# Madison Mcintosh, mcintosh@nisiaenean.net
# Montana Powell, montanap@semmagna.org
# Rogan Robinson, rr.robinson@xyz.edu
# Simon Rivera, sri@xyz.edu
# Benedict Pacheco, bpacheco@xyz.edu
# Maisie Hendrix, mai.hendrix@xyz.edu
# Xaviera Gould, xlg@utnisia.net
# Oren Rollins, oren@semmagna.com
# Flavia Santiago, flavia@utnisia.net
# Jackson Owens, jackowens@xyz.edu
# Britanni Humphrey, britanni@ut.net
# Kirk Nixon, kirknixon@xyz.edu
# Bree Campbell, breee@utnisia.net
# student-02-21656fe22197@linux-instance:~/scripts$ nano script.py

#!/usr/bin/env python3

import re
import csv

with open("user_emails.csv", 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()

# def contains_domain(address, domain):
#   """Returns True if the email address contains the given,domain,in the domain position, false if not."""
#   domain = r'[\w\.-]+@'+domain+'$'
#   if re.match(domain,address):
#     return True
#   return False


# def replace_domain(address, old_domain, new_domain):
#   """Replaces the old domain with the new domain in the received address."""
#   old_domain_pattern = r'' + old_domain + '$'
#   address = re.sub(old_domain_pattern, new_domain, address)
#   return address

# def main():
#   """Processes the list of emails, replacing any instances of the old domain with the new domain."""
#   old_domain, new_domain = 'abc.edu', 'xyz.edu'
#   csv_file_location = '/home/student-02-21656fe22197/data/user_emails.csv'
#   report_file = '/home/student-02-21656fe22197/data' + '/updated_user_emails.csv'
#   user_email_list = []
#   old_domain_email_list = []
#   new_domain_email_list = []

#   with open(csv_file_location, 'r') as f:
#     user_data_list = list(csv.reader(f))
#     user_email_list = [data[1].strip() for data in user_data_list[1:]]

#     for email_address in user_email_list:
#       if contains_domain(email_address, old_domain):
#         old_domain_email_list.append(email_address)
#         replaced_email = replace_domain(email_address,old_domain,new_domain)
#         new_domain_email_list.append(replaced_email)

#     email_key = ' ' + 'Email Address'
#     email_index = user_data_list[0].index(email_key)

#     for user in user_data_list[1:]:
#       for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
#         if user[email_index] == ' ' + old_domain:
#           user[email_index] = ' ' + new_domain
#   f.close()

#   with open(report_file, 'w+') as output_file:
#     writer = csv.writer(output_file)
#     writer.writerows(user_data_list)
#     output_file.close()

# main()