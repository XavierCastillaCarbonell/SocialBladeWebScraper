#set up
import os
import csv
import time

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

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
headers = {'User-Agent': user_agent}

#Scraper for common information

from commonScraper import CommonScraper

commonScraper = CommonScraper()

write(destinationDir, commonScraper.outputFileName, commonScraper.scrape(headers))


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
