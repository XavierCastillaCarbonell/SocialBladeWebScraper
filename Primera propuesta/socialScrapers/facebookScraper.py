# Import libraries
import requests
from bs4 import BeautifulSoup

class FacebookScraper(object):
	"""docstring for YoutubeScrapper"""
	def __init__(self):
		self.url = 'https://socialblade.com/facebook/'
		self.outputFileName = "TopInfluencersFacebook.csv"

	# Funcion que tiene como objetivo extraer los datos de la pagina
	def scrape(self):
		response = requests.get(self.url)
		soup = BeautifulSoup(response.content,'html.parser')
		container = soup.find("div", attrs={'class':'section-full-width'})
		elementList = [["Rank", "Grade", "User name", "Category", "Likes", "Talking about"]]

		for content in container.find_all("div", attrs={'class':'table-body'}):
			rank = content.find("div", attrs={'class':'section-rank'})
			grade = rank.find_next_sibling()
			name = grade.find_next_sibling()
			category = name.find_next_sibling()
			likes = category.find_next_sibling()
			talking = likes.find_next_sibling()

			row = [rank.get_text(),grade.get_text(),name.get_text(),category.get_text(),likes.get_text(),talking.get_text()]
			elementList.append(row)

		return elementList
