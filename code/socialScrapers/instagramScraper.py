# Import libraries
import requests
from commonScraper import CommonScraper
from bs4 import BeautifulSoup

class InstagramScraper(CommonScraper):
	"""docstring for YoutubeScrapper"""
	def __init__(self):
		url = 'https://socialblade.com/instagram/'
		outputFileName = "TopInfluencersInstagram.csv"
		super().__init__(url, outputFileName)

	# Funcion que tiene como objetivo extraer los datos de la pagina
	def scrape(self, headers):
		if(self.allowed):
			response = requests.get(self.url, headers = headers)
			soup = BeautifulSoup(response.content,'html.parser')
			container = soup.find("div", attrs={'class':'section-full-width'})
			elementList = [["Rank", "Grade", "User name", "Display name", "Media", "Followers", "Following"]]

			for content in container.find_all("div", attrs={'class':'table-body'}):
				rank = content.find("div", attrs={'class':'section-rank'})
				grade = rank.find_next_sibling()
				name = grade.find_next_sibling()
				displayName = name.find_next_sibling()
				media = displayName.find_next_sibling()
				followers = media.find_next_sibling()
				following = followers.find_next_sibling()

				row = [rank.get_text(),grade.get_text(),name.get_text(),displayName.get_text(),media.get_text(),followers.get_text(),following.get_text()]
				elementList.append(row)

			return elementList
		else:
			print("We can not scrape the Instagram page")
			return ["Not possible to scrape"]
