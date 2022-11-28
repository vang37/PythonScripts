from bs4 import BeautifulSoup
import requests

source = requests.get('https://avc.com').text 
	
soup = BeautifulSoup(source, 'lxml')
	
#post = soup.find('div', class_='archives-by-month')
	
#for link in soup.find_all('a', href=True):
#	print(link['href'])

for y in range(2003,2020): 
	for s in range(1,13): 
		words = requests.get('https://avc.com/' + str(y) + '/' + "{:02d}".format(s) +'/').text
		soup2 = BeautifulSoup(words, 'lxml')
		for link in soup2.find_all('h2', class_="post-title"):
			print(link.text)