import requests
from bs4 import *

animelink = input("Enter Link of your Anime Series : ")  #User Enters URL

start = int(input("Enter Episode Number to start with : "))
end = int(input("Enter Episode Number to end with : "))
print("Generating Links from", start, "to", end) 
end=end+1 # Increased by 1 for range function

animename = animelink.split("/")  #splits link by /
URL_PATTERN = 'https://www.gogoanimes.co/{}-episode-{}' #General URL pattern for every anime on gogoanime
for episode in range(start,end):
    url = URL_PATTERN.format(animename[4],episode)
    srcCode = requests.get(url)
    plainText = srcCode.text
    soup = BeautifulSoup(plainText,"lxml")
    try:
        source_url = soup.find('div', {'class': 'download-anime'}).find('a')     #get element with 'a' tag
        link = source_url.get('href')
        dowCode = requests.get(link)
        data = dowCode.text
        soup = BeautifulSoup(data,"lxml")
        dow_url = soup.findAll('div', {'class': 'dowload'})[2].find('a')     #get 3rd elements with 'a' tag
        dowlink = dow_url.get('href')
        print(dowlink)
        f = open('{}.txt'.format(animename[4]),"a") #opens file with name of "test.txt"
        f.write(dowlink+"\n\n")
    except:
        print("Episode {} Does Not Exist!".format(episode))

f.close()
