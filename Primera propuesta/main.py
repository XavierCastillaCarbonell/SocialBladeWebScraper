#set up
import os
import csv
import time
import requests
from random import choice

os.system('start /wait cmd /c ' + 'pip install ' + 'requests')
os.system('start /wait cmd /c ' + 'pip install ' + 'beautifulsoup4')

#Write Function
def write(destinationDir, outputFileName, elementList):
	currentDir = os.path.dirname(__file__)
	if not os.path.exists(destinationDir):
		os.makedirs(destinationDir)
	filePath = os.path.join(currentDir, destinationDir+'/'+outputFileName)
	with open(filePath, 'w', newline='') as csvFile:
		writer = csv.writer(csvFile)
		for element in elementList:
			try:
				writer.writerow(element)
			except:
  				print("An exception occurred while writing some registers (most common: special character)")

destinationDir = "output" #name of the output directory

# Creamos una lista de user_agents (https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent)
user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

headers = {'User-Agent': choice(user_agents)}

#Scraper for common information
from commonScraper import CommonScraper

commonScraper = CommonScraper(url = 'https://socialblade.com', outputFileName = "TopInfluencers.csv")

#Scrapers for each page
from socialScrapers.youtubeScraper import YoutubeScraper
from socialScrapers.twitchScraper import TwitchScraper
from socialScrapers.twitterScraper import TwitterScraper
from socialScrapers.instagramScraper import InstagramScraper
from socialScrapers.facebookScraper import FacebookScraper
from socialScrapers.dailymotionScraper import DailymotionScraper
from socialScrapers.mixerScraper import MixerScraper

youtubeScraper = YoutubeScraper()
twitchScraper = TwitchScraper()
twitterScraper = TwitterScraper()
instagramScraper = InstagramScraper()
facebookScraper = FacebookScraper()
dailymotionScraper = DailymotionScraper()
mixerScraper = MixerScraper()

url = 'https://socialblade.com/robots.txt'

while True:
    print("bla bla bla")
    lines = requests.get(url).text.splitlines()

    for line in lines:
        if 'Disallow:' in line:
            line = line[10:]
            if line == "/youtube":
                youtubeScraper.disallow()
                print('Youtube no se debe procesar')
            elif line == "/twitch":
                twitchScraper.disallow()
                print('Twitch no se debe procesar')
            elif line == "/twitter":
                twitterScraper.disallow()
                print('Twitter no se debe procesar')
            elif line == "/instagram":
                instagramScraper.disallow()
                print('Instagram no se debe procesar')
            elif line == "/dailymotion":
                dailymotionScraper.disallow()
                print('Dailymotion no se debe procesar')
            elif line == "/mixer":
                mixerScraper.disallow()
                print('Mixer no se debe procesar')
            elif line == "/facebook":
                facebookScraper.disallow()
                print('Facebook no se debe procesar')

    write(destinationDir, commonScraper.outputFileName, commonScraper.scrape(headers)) # commonScraper ya tiene sleep() internos

    write(destinationDir, youtubeScraper.outputFileName, youtubeScraper.scrape(headers))
    time.sleep(0.2) # Ponemos un tiempo de espera entre cada peticion para evitar saturar el servidor

    write(destinationDir, twitchScraper.outputFileName, twitchScraper.scrape(headers))
    time.sleep(0.2) # Ponemos un tiempo de espera entre cada peticion para evitar saturar el servidor

    write(destinationDir, twitterScraper.outputFileName, twitterScraper.scrape(headers))
    time.sleep(0.2) # Ponemos un tiempo de espera entre cada peticion para evitar saturar el servidor

    write(destinationDir, instagramScraper.outputFileName, instagramScraper.scrape(headers))
    time.sleep(0.2) # Ponemos un tiempo de espera entre cada peticion para evitar saturar el servidor

    write(destinationDir, facebookScraper.outputFileName, facebookScraper.scrape(headers))
    time.sleep(0.2) # Ponemos un tiempo de espera entre cada peticion para evitar saturar el servidor

    write(destinationDir, dailymotionScraper.outputFileName, dailymotionScraper.scrape(headers))
    time.sleep(0.2) # Ponemos un tiempo de espera entre cada peticion para evitar saturar el servidor

    write(destinationDir, mixerScraper.outputFileName, mixerScraper.scrape(headers))

    # Volvemos a activar todos los scrapers en caso de que los permisos del robots.txt cambien en un futuro
    youtubeScraper.allow()
    twitchScraper.allow()
    twitterScraper.allow()
    instagramScraper.allow()
    facebookScraper.allow()
    dailymotionScraper.allow()
    mixerScraper.allow()

    time.sleep(3600) # Esperamos una hora para hacer la siguiente iteración de scrape
