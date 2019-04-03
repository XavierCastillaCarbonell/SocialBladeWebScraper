# Import libraries
import requests
from bs4 import BeautifulSoup

class TwitchScraper(object):
	"""docstring for YoutubeScrapper"""
	def __init__(self):
		self.url = 'https://socialblade.com/twitch/'
		self.outputFileName = "TopInfluencersTwitch.csv"

	# Funcion que tiene como objetivo extraer los datos de la pagina
	def scrape(self):
		response = requests.get(self.url)
		soup = BeautifulSoup(response.content,'html.parser')
		container = soup.find("div", attrs={'class':'section-full-width'})
		elementList = [["Rank", "Grade", "User name", "Last game", "Views", "Followers"]]

		for content in container.find_all("div", attrs={'class':'table-body'}):
			rank = content.find("div", attrs={'class':'section-rank'})
			grade = rank.find_next_sibling()
			name = grade.find_next_sibling()
			lastGame = name.find_next_sibling()
			views = lastGame.find_next_sibling()
			followers = lastGame.find_next_sibling()

			row = [rank.get_text(),grade.get_text(),name.get_text(),lastGame.get_text(),views.get_text(),followers.get_text()]
			elementList.append(row)

		return elementList
