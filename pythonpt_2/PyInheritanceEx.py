



# import random

# class Server:
#     def __init__(self):
#         """Creates a new server instance, with no active connections."""
#         self.connections = {}

#     def add_connection(self, connection_id):
#         """Adds a new connection to this server."""
#         connection_load = random.random()*10+1
#         self.connections[connection_id] = connection_load
#         # Add the connection to the dictionary with the calculated load

#     def close_connection(self, connection_id):
#         """Closes a connection on this server."""
#         # Remove the connection from the dictionary

#     def load(self):
#         """Calculates the current load for all connections."""
#         total = 0
#         for value in self.connections.values():
#             total += value
#         # Add up the load for each of the connections
#         return total

#     def __str__(self):
#         """Returns a string with the current load of the server"""
#         return "{:.2f}%".format(self.load())

# server = Server()
# server.add_connection("192.168.1.1")

# # print(server.load())

# class LoadBalancing:
#     def __init__(self):
#         """Initialize the load balancing system with one server"""
#         self.connections = {}
#         self.servers = [Server()]

#     def add_connection(self, connection_id):
#         """Randomly selects a server and adds a connection to it."""
#         server = random.choice(self.servers)
#         self.connections[connection_id] = server
#         server.add_connection(connection_id)
#         if self.ensure_availability() == True:
#             self.servers.append(Server())
#         # Add the connection to the dictionary with the selected server
#         # Add the connection to the server

#     def close_connection(self, connection_id):
#         server = self.connections[connection_id]
#         server.close_connection(connection_id)
#         del self.connections[connection_id]
#         # Find out the right server
#         # Close the connection on the server
#         # Remove the connection from the load balancer

#     def avg_load(self):
#         """Calculates the average load of all servers"""
#         total = 0
#         for value in self.servers:
#             total += value.load()
#         return total/len(self.servers)
#         # Sum the load of each server and divide by the amount of servers

#     def ensure_availability(self):
#         """If the average load is higher than 50, spin up a new server"""
#         if self.avg_load() > 50:
#             return True
#         else:
#             return False


#     def __str__(self):
#         """Returns a string with the load for each server."""
#         loads = [str(server) for server in self.servers]
#         return "[{}]".format(",".join(loads))


# l = LoadBalancing()
# l.add_connection("fdca:83d2::f20d")
# # print(l.avg_load())

# l.servers.append(Server())
# # print(l.avg_load())

# l.close_connection("fdca:83d2::f20d")
# # print(l.avg_load())

# for connection in range(20):
#     l.add_connection(connection)
# print(l)

# print(l.avg_load())

# def get_event_date(event):
#   return event.date

# def current_users(events):
#   events.sort(key=get_event_date)
#   machines = {}
#   for event in events:
#     if event.machine not in machines:
#       machines[event.machine] = set()
#     if event.type == "login":
#       machines[event.machine].add(event.user)
#     elif event.type == "logout" and event.user in machines[event.machine]:
#       machines[event.machine].remove(event.user)
#   return machines

# def generate_report(machines):
#   for machine, users in machines.items():
#     if len(users) > 0:
#       user_list = ", ".join(users)
#       print("{}: {}".format(machine, user_list))

# class Event:
#   def __init__(self, event_date, event_type, machine_name, user):
#     self.date = event_date
#     self.type = event_type
#     self.machine = machine_name
#     self.user = user

# events = [
#     Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
#     Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
#     Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
#     Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
#     Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
#     Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
# ]

# users = current_users(events)
# # print(users)

# generate_report(users)





# clean_words = []
# new_clean_words = []

# import string
# import re
# import operator

# filename = 'ulyss11.txt'
# file = open(filename, 'rt')
# text = file.read()
# file.close()
# words = text.split()[2343:]

# for word in words:
#   clean_words += re.split("[']", word)

# table = str.maketrans(" ", " ", string.punctuation)
# stripped = [w.lower().translate(table) for w in clean_words]

# stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn'] + ['said'] + ['asked'] + ['good', 'like', 'mr', 'one', 'says', 'man', 'two', 'would', 'back', 'know', 'could', 'street', 'little', 'first', 'way', 'well', 'come', 'say', 'get', 'us', 'never', 'long', 'round', 'right', 'must', 'sir', 'put', 'let', 'mrs', 'thing', 'going', 'came', 'still', 'young', 'made', 'went', 'got', 'something', 'voice', 'tell', 'might', 'three', 'make', 'give', 'house', 'though', 'course', 'much', 'left', 'ever', 'saw', 'hands', 'men', 'want', 'behind', 'told', 'think', 'take', 'fellow', 'every', 'took', 'bit', 'door', 'without', 'turned', 'till', 'place', 'miss', 'better', 'best', 'upon', 'great', 'heard', 'even', 'gave', 'half', 'coming', 'big', 'towards', 'thought', 'near', 'looking', 'word', 'call', 'looked', 'things', 'knew', 'side']


# new_clean_words = [w for w in stripped if not w in stop_words and w != '']


# def count_letters(text):
#   result = {}
#   for l in text:
#     if l not in result:
#         result[l] = 0
#     result[l] += 1
#   return result

# sorted_d = dict(sorted(count_letters(new_clean_words).items(), key=operator.itemgetter(1),reverse=True))

# print(sorted_d)

# !pip install wordcloud
# !pip install fileupload
# !pip install ipywidgets
# !jupyter nbextension install --py --user fileupload
# !jupyter nbextension enable --py fileupload

# import wordcloud
# import numpy as np
# from matplotlib import pyplot as plt
# from IPython.display import display
# import fileupload
# import io
# import sys
# import string

# # This is the uploader widget

# def _upload():

#     _upload_widget = fileupload.FileUploadWidget()

#     def _cb(change):
#         global file_contents
#         decoded = io.StringIO(change['owner'].data.decode('utf-8'))
#         filename = change['owner'].filename
#         print('Uploaded `{}` ({:.2f} kB)'.format(
#             filename, len(decoded.read()) / 2 **10))
#         file_contents = decoded.getvalue()

#     _upload_widget.observe(_cb, names='data')
#     display(_upload_widget)

# _upload()

# def count_letters(text):
#   result = {}
#   for l in text:
#     if l not in result:
#         result[l] = 0
#     result[l] += 1
#   return result

# def calculate_frequencies(file_contents):
#     # Here is a list of punctuations and uninteresting words you can use to process your text
#     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#     uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
#     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
#     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
#     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
#     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

#     # LEARNER CODE START HERE
#     words = file_contents.split()
#     table = str.maketrans(" ", " ", string.punctuation)
#     stripped = [w.lower().translate(table) for w in words]
#     clean_words = [w for w in stripped if not w in uninteresting_words and w != '']

#     #wordcloud
#     cloud = wordcloud.WordCloud()
#     cloud.generate_from_frequencies()
#     return cloud.to_array()

# # Display your wordcloud image

# myimage = calculate_frequencies(file_contents)
# plt.imshow(myimage, interpolation = 'nearest')
# plt.axis('off')
# plt.show()






# import numpy as np
# a = np.random.randn(4, 3) # a.shape = (4, 3)
# b = np.random.randn(3, 1) # b.shape = (3, 2)
# c = a*b
# print(c)

# a = np.array([[18, 15, 15],[18, 25, 16],[9,  5,  25]])
# b = np.array([[3],[6],[4]])
# c = b*a #[[ 54  45  45][108 150  96][ 36  20 100]] 
# d = np.dot(a, b)
# print("a: ", a, "b: ", b)
# print("c: ", c, "d: ", d)

# A = np.random.randn(4,3)
# B = np.sum(A, axis = 1, keepdims = True)
# print("B.shape: ", B.shape)
# a = np.random.randn(12288, 150) # a.shape = (12288, 150)
# b = np.random.randn(150, 45) # b.shape = (150, 45)
# c = np.dot(a,b)
# print(c.shape)

# for l in range(1,10):
#     print(l)

#import the necessary packages and modules
# import numpy as np
# import matplotlib.pyplot as plt

# #define the function f(x,y)
# def f(x, y):
#     return 2*np.square(x) + 5*np.square(y)

# #define the domain of interest, and the size of the mesh
# domain_of_interest_x = (-5, 5)
# domain_of_interest_y = (-5, 5)
# grid_size = 0.1

# #generate the mesh points with the np.meshgrid() function
# mesh_points_x, mesh_points_y = np.meshgrid(np.arange(domain_of_interest_x[0], domain_of_interest_x[1], grid_size), np.arange(domain_of_interest_y[0], domain_of_interest_y[1], grid_size))

# #calculate the value of f(x, y) over the mesh points
# Z = f(mesh_points_x.ravel(), mesh_points_y.ravel())

# #reshape and plug into the plt.contour() function
# Z = Z.reshape(mesh_points_x.shape)
# plt.contour(mesh_points_x, mesh_points_y, Z, levels=[1, 5, 9, 13, 17, 29], cmap=plt.cm.Spectral)

# a = np.random.randn(2, 3) # a.shape = (2, 3)
# b = np.random.randn(2, 1) # b.shape = (2, 1)
# c = a + b
# print("a: ", a, "b: ",b, "c: ", c)




