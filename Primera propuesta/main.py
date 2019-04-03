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
  				print("An exception occurred")

destinationDir = "output" #name of the output directory

#Scraper for common information

from commonScraper import CommonScraper

commonScraper = CommonScraper()

write(destinationDir, commonScraper.outputFileName, commonScraper.scrape())


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

write(destinationDir, youtubeScraper.outputFileName, youtubeScraper.scrape())
time.sleep(0.2) # Ponemos un tiempo de espera entre cada peticion para evitar saturar el servidor
write(destinationDir, twitchScraper.outputFileName, twitchScraper.scrape())
time.sleep(0.2) # Ponemos un tiempo de espera entre cada peticion para evitar saturar el servidor
write(destinationDir, twitterScraper.outputFileName, twitterScraper.scrape())
time.sleep(0.2) # Ponemos un tiempo de espera entre cada peticion para evitar saturar el servidor
write(destinationDir, instagramScraper.outputFileName, instagramScraper.scrape())
time.sleep(0.2) # Ponemos un tiempo de espera entre cada peticion para evitar saturar el servidor
write(destinationDir, facebookScraper.outputFileName, facebookScraper.scrape())
time.sleep(0.2) # Ponemos un tiempo de espera entre cada peticion para evitar saturar el servidor
write(destinationDir, dailymotionScraper.outputFileName, dailymotionScraper.scrape())
time.sleep(0.2) # Ponemos un tiempo de espera entre cada peticion para evitar saturar el servidor
write(destinationDir, mixerScraper.outputFileName, mixerScraper.scrape())
