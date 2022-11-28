# from docx import Document

# document = Document('multipleParagraphs.docx')

# for i in range(len(document.paragraphs)):
#     print(document.paragraphs[i].text)

# from PIL import Image
# import os, glob

# cwd = os.getcwd()

# for entry in glob.glob(cwd + "/images/" + "*"):
#     f = os.path.splitext(os.path.basename(entry))[0]
#     print(f)
#     im = Image.open(entry).convert('RGB').resize((640,480)).rotate(270)
#     im.save("/Users/new_image/{}.jpg".format(f), "JPEG")


import os
import requests

pwd = "/Users/G_Hughes/Desktop/new_image/"
file_array = os.listdir(pwd)

title_array = ["title:", "name:", "date:", "feedback:"]
dictionary = {}


for entry in file_array:
    print(entry)
    with open(pwd + entry, "r") as f:
        array = f.readlines()
        for i in range(len(array)):
            dictionary[title_array[i]] = array[i].strip()
        print(dictionary)

if item["total_sales"] > max_sales["total_sales"]:
    max_sales = item

car_sales = {}


def car_year_calc(car, total_sales):
    if(car["car_year"] in car_sales):
        car_sales[car["car_year"]] = car_sales[car["car_year"]]+total_sales
    else:
        car_sales[car["car_year"]] = total_sales


car_year_calc(item["car"], item["total_sales"])


def most_popular_year():
    var = ''
    val = 0
    for v in car_sales:
        if(car_sales[v] > val):
            var = v
            val = car_sales[var]
    return "The most popular year was " + str(var) + " with " + str(val) + " sales."

    "The {} had the most sales: {}".format(
        format_car(max_sales["car"]), max_sales["total_sales"]),
    most_popular_year()

    #     class Dictionary:
    #         def __init__(self, title, name, date, feedback):
    #             self.t = title
    #             self.n = name
    #             self.d = date
    #             self.f = feedback

    # print(Dictionary(array[0], array[1], array[2], array[3]))


def pdf_generator(summary, data):
    table_data = cars_dict_to_table(data)
    result = ''
    for line in summary:
        result = result+line+'<br/>'
    reports.generate(
        "/tmp/cars.pdf", "Sales Summary for last month", result, table_data)


def email_generated_report(summary):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Sales summary for last month"
    body = '\n'.join(summary)
    message = emails.generate(
        sender, receiver, subject, body, "/tmp/cars.pdf")
    emails.send(message)

pdf_generator(summary,data)

import emails
import os
import reports

max_sales = {"total_sales": 0}

import os
from PIL import Image

path = "/home/student-01-847ab28fd5a3/supplier-data/images"

for file in os.listdir(path):
  base = os.path.basename(file)
  full_path = os.path.join(path, file)
  if ".tiff" in base:
    im = Image.open(full_path)
    im_new = im.resize((600,400)).convert("RGB")
    name = os.path.splitext(base)[0]
    new_file = path + "/" + name + ".jpeg"
    im_new.save(new_file, "JPEG")

#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"

path = "/home/student-01-847ab28fd5a3/supplier-data/images"

for file in os.listdir(path):
  if ".jpeg" in os.path.basename(file):
    full_path = os.path.join(path,file)
    with open(full_path, "rb") as opened:
      response = requests.post(url, files={'file': opened})
      print(response.status_code)

#!/usr/bin/env python3
import os
import requests
import json

path = "/home/student-01-847ab28fd5a3/supplier-data/descriptions"
img_path = "/home/student-01-847ab28fd5a3/supplier-data/images"

dict_keys = ["name", "weight", "description","image_name"]
my_dict = {}

for txt_file in os.listdir(path):
  key_count = 0
  full_path = os.path.join(path,txt_file)
  respective_img = os.path.splitext(txt_file)[0]+'.jpeg'
  with open(full_path) as f:
    for line in f:
      if key_count == 1:
        line = int(line.strip("lbs\n"))
      else:
        line = line.strip("\n")
      my_dict[dict_keys[key_count]] = line
      key_count +=1
    my_dict[dict_keys[3]] = respective_img
  response = requests.post("http://35.238.59.118/fruits/", data = my_dict)
  print(response.status_code)

#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
  report = SimpleDocTemplate(attachment)
  styles = getSampleStyleSheet()
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(paragraph, styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info])

#!/usr/bin/env python3
import os
import reports
import sys
from datetime import date
import emails

path = "/home/student-01-847ab28fd5a3/supplier-data/descriptions"

def main(argv):
  string = ""
  for file in os.listdir(path):
    full_path = os.path.join(path,file)
    with open(full_path) as text_file:
      count = 0
      for line in text_file:
        if count == 0:
          string += "name: {}".format(line)+"<br/>"
          count+=1
        elif count == 1:
          string += "weight: {}".format(line)+"<br/>"
          count +=1

  paragraph = string
  print(paragraph)
  attachment = "/tmp/processed.pdf"
  today = date.today()
  today_format = today.strftime("%B %d, %Y")
  title = "Processed Update on: {}".format(today_format)
  reports.generate_report(attachment, title, paragraph)

  sender = "automation@example.com"
  recipient = "student-01-847ab28fd5a3@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = "/tmp/processed.pdf"
  message = emails.generate_email(sender, recipient, subject, body, attachment)
  emails.send_email(message)

if __name__ == "__main__":
  main(sys.argv)

#!/usr/bin/env python3
import email.message
import mimetypes
import os.path
import smtplib

def generate_email(sender, recipient, subject, body, attachment_path):
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  if not attachment_path == "":
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
      message.add_attachment(ap.read(), maintype = mime_type, subtype = mime_subtype, filename = attachment_filename)
  return message

def send_email(message):
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()

#!/usr/bin/env python3
import shutil
import psutil
import os
import socket
import emails

def check_cpu_usage():
  return psutil.cpu_percent(1) < 80

def check_disk_space():
  disk = "/"
  min_percent = 20
  d_use = shutil.disk_usage(disk)
  percent_free = 100*d_use.free / d_use.total
  return percent_free > 20

def check_memory_usage():
  free = psutil.virtual_memory().available
  available_memory = (free/1024) / 1024
  return available_memory > 500

def check_resolve_hostname():
  host_name = socket.gethostbyname('localhost')
  return host_name == '127.0.0.1'

def checks():
  if not check_disk_space():
      subject = 'Error - Available disk space is less than 20%'
      return subject
  elif not check_cpu_usage():
      subject = 'Error - CPU usage is over 80%'
      return subject
  elif not check_memory_usage():
      subject = 'Error - Available memory is less than 500MB'
      return subject
  elif not check_resolve_hostname():
      subject = 'Error - localhost cannot be resolved to 127.0.0.1'
      return subject
  else:
      return None

if __name__ == "__main__":
    USER = os.getenv('USER')
    subject = checks()
    if subject is not None:
        body = 'Please check your system and resolve the issue as soon as possible.'
        message = emails.generate_email("automation@example.com", "{}@example.com".format(USER), subject, body, "")
        emails.send_email(message)