# Import libraries
import requests
from bs4 import BeautifulSoup

class YoutubeScraper(object):
	"""docstring for YoutubeScrapper"""
	def __init__(self):
		self.url = 'https://socialblade.com/youtube/'
		self.outputFileName = "youtube.csv"

	def scrape(self):
		response = requests.get(self.url)
		soup = BeautifulSoup(response.content,'html.parser')
		container = soup.find("div", attrs={'class':'section-full-width'})
		elementList=[]

		for content in container.find_all("div", attrs={'class':'table-body'}):
			rank = content.find("div", attrs={'class':'section-rank'})
			grade = rank.find_next_sibling()
			name = grade.find_next_sibling()
			videos = name.find_next_sibling()
			subscribers = videos.find_next_sibling()
			views = subscribers.find_next_sibling()

			row = [rank.get_text(),grade.get_text(),name.get_text(),videos.get_text(),subscribers.get_text(),views.get_text()]
			elementList.append(row)

		return elementList
