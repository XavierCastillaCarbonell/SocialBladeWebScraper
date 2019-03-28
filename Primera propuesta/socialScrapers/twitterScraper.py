# Import libraries
import requests
from bs4 import BeautifulSoup

class TwitterScraper(object):
	"""docstring for YoutubeScrapper"""
	def __init__(self):
		self.url = 'https://socialblade.com/twitter/'
		self.outputFileName = "twitter.csv"

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
			displayName = name.find_next_sibling()
			tweets = displayName.find_next_sibling()
			followers = tweets.find_next_sibling()
			following = followers.find_next_sibling()

			row = [rank.get_text(),grade.get_text(),name.get_text(),displayName.get_text(),tweets.get_text(),followers.get_text(),following.get_text()]
			elementList.append(row)

		return elementList
