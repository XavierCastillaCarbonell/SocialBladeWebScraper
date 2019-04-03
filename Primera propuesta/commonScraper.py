# Import libraries
import requests
from bs4 import BeautifulSoup

class CommonScraper(object):
	"""docstring for YoutubeScrapper"""
	def __init__(self):
		self.url = 'https://socialblade.com'
		self.outputFileName = "TopInfluencers.csv"

	#Como cada una de las paginas tiene en una ubicación distinta la columna de subscriptores es necesario un extractor concreto para cada una de ellas
	def _getFollowersByPlatform(self, link, content):
		if link == '/youtube':
			return content.find("div", attrs={'class':'table-cell section-lg'}).find_next_sibling().get_text()
		elif link == '/twitch':
			return content.find("div", attrs={'class':'table-cell section-lg'}).find_next_sibling().get_text()
		elif link == '/twitter':
			return content.find("div", attrs={'class':'table-cell section-sm'}).find_next_sibling().get_text()
		elif link == '/instagram':
			return content.find("div", attrs={'class':'table-cell section-sm'}).find_next_sibling().get_text()
		elif link == '/facebook': 
			return "NA"
		elif link == '/dailymotion':
			return content.find("div", attrs={'class':'table-cell section-sm'}).find_next_sibling().get_text()
		elif link == '/mixer':
			return content.find("div", attrs={'class':'table-cell section-med'}).find_next_sibling().get_text()
		else: 
			return "ERROR: Platform not suported: " + link

	# Funcion que tiene como objetivo extraer los datos de la pagina
	def scrape(self):
		elementList = [["Rank", "Grade", "Name", "Followers"]]
		response = requests.get(self.url)
		soup = BeautifulSoup(response.content,'html.parser')
		contentCharts = soup.find("div", attrs={'id':'top-menu-content-charts'})

		for elem in contentCharts.find_all("a"):
			link = elem.get('href')
			newResponse = requests.get(self.url+link)
			newSoup = BeautifulSoup(newResponse.content,'html.parser')
			container = newSoup.find("div", attrs={'class':'section-full-width'})

			for content in container.find_all("div", attrs={'class':'table-body'}):
				rank = content.find("div", attrs={'class':'section-rank'})
				grade = rank.find_next_sibling()
				name = grade.find_next_sibling()
				followers = self._getFollowersByPlatform(link, content)

				row = [rank.get_text(),grade.get_text(),name.get_text(),followers]
				elementList.append(row)
		
		return elementList
