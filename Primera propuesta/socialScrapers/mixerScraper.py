# Import libraries
import requests
from bs4 import BeautifulSoup

class MixerScraper(object):
	"""docstring for YoutubeScrapper"""
	def __init__(self):
		self.url = 'https://socialblade.com/mixer/'
		self.outputFileName = "TopInfluencersMixer.csv"

	# Funcion que tiene como objetivo extraer los datos de la pagina
	def scrape(self):
		response = requests.get(self.url)
		soup = BeautifulSoup(response.content,'html.parser')
		container = soup.find("div", attrs={'class':'section-full-width'})
		elementList = [["Rank", "Grade", "User name", "Followers", "Channel views", "Level", "Latest game"]]

		for content in container.find_all("div", attrs={'class':'table-body'}):
			rank = content.find("div", attrs={'class':'section-rank'})
			grade = rank.find_next_sibling()
			name = grade.find_next_sibling()
			followers = name.find_next_sibling()
			channelViews = followers.find_next_sibling()
			level = channelViews.find_next_sibling()
			latestGame = level.find_next_sibling()

			row = [rank.get_text(),grade.get_text(),name.get_text(),followers.get_text(),channelViews.get_text(),level.get_text(),latestGame.get_text()]
			elementList.append(row)

		return elementList
