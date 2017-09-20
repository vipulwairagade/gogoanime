import requests
from bs4 import *

animelink = raw_input("Enter Link of your Anime Series : ")

start = int(input("Enter Episode Number to start with : "))
end = int(input("Enter Episode Number to end with : "))
print "Generating Links from", start, "to", end 
end=end+1

#https://ww3.gogoanime.io/category/boruto-naruto-next-generations
animename = animelink.split("/")


links = []
URL_PATTERN = 'https://ww3.gogoanime.io/{}-episode-{}'
for episode in range(start,end):
	url = URL_PATTERN.format(animename[4],episode)
	srcCode = requests.get(url)
	plainText = srcCode.text
	soup = BeautifulSoup(plainText,"lxml")
	source_url = soup.find('div', {'class': 'download-anime'}).find('a')     #get all elements with 'a' tag
	link = source_url.get('href')
	links.append(link)
	print link
	
for dowurl in links:
	dowCode = requests.get(dowurl)
	data = dowCode.text
	soup = BeautifulSoup(data,"lxml")
	dow_url = soup.findAll('div', {'class': 'dowload'})[2].find('a')     #get all elements with 'a' tag
	dowlink = dow_url.get('href')
	print dowlink
	f = open("dowlink.txt","a") #opens file with name of "test.txt"
	f.write(dowlink+"\n\n")

f.close()

