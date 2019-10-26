import requests
from bs4 import *

animelink = input("Enter Link of your Anime Series : ")  # User Enters URL

start = int(input("Enter Episode Number to start with : "))
end = int(input("Enter Episode Number to end with : "))
print("Generating Links from", start, "to", end) 
end=end+1 # Increased by 1 for range function

animename = animelink.split("/")[-1].split("-episode")[0]  # splits link by / and takes the name, removes episodes
URL_PATTERN = 'https://www.gogoanime.io/{}-episode-{}' # General URL pattern for every anime on gogoanime
for episode in range(start,end):
    url = URL_PATTERN.format(animename,episode)
    srcCode = requests.get(url)
    plainText = srcCode.text
    if "Page not found" in plainText:
        print("Missing {} Episode {}".format(animename,episode))
        continue # skip this one and go to next episode
    soup = BeautifulSoup(plainText,"html.parser")
    source_url = soup.find('span', {'class': 'btndownload'}).parent # get element with 'a' tag
    link = source_url.get('href')
    dowCode = requests.get(link)
    data = dowCode.text
    soup = BeautifulSoup(data,"html.parser")
    dow_url = soup.findAll('div', {'class': 'dowload'})[2].find('a') # get 3rd elements with 'a' tag
    dowlink = dow_url.get('href')
    print(dowlink)
    f = open('{}.txt'.format(animename.replace("-"," ").title()),"a") # opens file with name of the anime formatted nicely
    f.write(dowlink+"\n\n")
    f.close()
