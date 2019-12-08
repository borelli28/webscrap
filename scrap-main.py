import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#request the url and saved the response
url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)

#parse html with beautifulsoup
soup = BeautifulSoup(response.text, "html.parser")
#use method findAll() to locate all <a> tags
soup.findAll("a")

#for loop to download the whole data set of tags
for i in range(36, len(soup.findAll("a"))+1):
    #extract the link we want
    one_a_tag = soup.findAll("a")[i]
    link = one_a_tag["href"]
    download_url = 'http://web.mta.info/developers/'+ link
    aol = urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
    #pause for one second between requests
    time.sleep(1)
    print(aol)
