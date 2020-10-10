from bs4 import BeautifulSoup
import requests
import urllib.request
import webbrowser


n = input("Enter the ID of the Footage : ")
url ="https://stock.adobe.com/search/video?filters%5Bcontent_type%3Aphoto%5D=0&filters%5Bcontent_type%3Aillustration%5D=0&filters%5Bcontent_type%3Azip_vector%5D=0&filters%5Bcontent_type%3Avideo%5D=1&filters%5Bcontent_type%3Atemplate%5D=0&filters%5Bcontent_type%3A3d%5D=0&filters%5Binclude_stock_enterprise%5D=0&filters%5Bis_editorial%5D=0&filters%5Bcontent_type%3Aimage%5D=0&order=relevance&safe_search=1&serie_id={}&search_page=1&search_type=see-more&limit=100&get_facets=0&asset_id={}".format(n,n)
open_in_web = urllib.request.urlopen(url)

webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open(url)

print("result Code :"+ str(open_in_web.getcode()))