# Import libraries
import requests
from commonScraper import CommonScraper
from bs4 import BeautifulSoup

class DailymotionScraper(CommonScraper):
	"""docstring for YoutubeScrapper"""
	def __init__(self):
		url = 'https://socialblade.com/dailymotion/'
		outputFileName = "TopInfluencersDailymotion.csv"
		super().__init__(url, outputFileName)

	# Funcion que tiene como objetivo extraer los datos de la pagina
	def scrape(self, headers):
		elementList = [["Rank", "Grade", "User name", "Display name", "Media", "Followers", "Vidviews"]]
		if(self.allowed):
			response = requests.get(self.url, headers = headers)
			soup = BeautifulSoup(response.content,'html.parser')
			container = soup.find("div", attrs={'class':'section-full-width'})

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
		else:
			print("We can not scrape the Dailymotion page")
			return ["Not possible to scrape"]
