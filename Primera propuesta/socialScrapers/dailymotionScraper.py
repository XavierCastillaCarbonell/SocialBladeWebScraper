# Import libraries
import requests
from bs4 import BeautifulSoup

class DailymotionScraper(object):
	"""docstring for YoutubeScrapper"""
	def __init__(self):
		self.url = 'https://socialblade.com/dailymotion/'
		self.outputFileName = "dailymotion.csv"

	# Funcion que tiene como objetivo extraer los datos de la pagina
	def scrape(self):
		response = requests.get(self.url)
		soup = BeautifulSoup(response.content,'html.parser')
		container = soup.find("div", attrs={'class':'section-full-width'})
		elementList=[]

		for content in container.find_all("div", attrs={'class':'table-body'}):
			rank = content.find("div", attrs={'class':'section-rank'})
			grade = rank.find_next_sibling()
			name = grade.find_next_sibling()
			displayname = name.find_next_sibling()
			media = displayname.find_next_sibling()
			followers = media.find_next_sibling()
			vidviews = followers.find_next_sibling()

			row = [rank.get_text(),grade.get_text(),name.get_text(),displayname.get_text(),media.get_text(),followers.get_text(),vidviews.get_text()]
			elementList.append(row)

		return elementList
