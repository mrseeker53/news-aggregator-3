import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def crawler(url):
	topic = str(input("Enter news topic: "))
	#Replace whitespace with a plus sign into user input topic
	#and add it to the url
	news_url = url + topic.replace(' ','+')
	print('\n\n')

	#Open a connection to a URL
	client = urlopen(news_url)
	#Read the data from the URL
	xml_page = client.read()		
	client.close()

	list = []
	#Soup - pull out/parse data of xml files
	page = soup(xml_page,"xml")
	#Matches of pattern in string are returned, as a list of strings
	all_links = page.findAll("item")

	for link in all_links:
		list.append(link)
	
	# Print top 3 news on the same topic with publish date, title & link
	for news in list[1:4]:
		print(news.pubDate.text)
		print(news.title.text) 
		print(news.link.text)
		print("-"*60)
	
url="https://news.google.com/rss/search?q="

#you can add google news 'xml' URL here for any country/category 
#news_url="https://news.google.com/news/rss/?ned=us&gl=US&hl=en"
#sports_url="https://news.google.com/news/rss/headlines/section/topic/SPORTS.en_in/Sports?ned=in&hl=en-IN&gl=IN"

crawler(url)	