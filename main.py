import requests 
from bs4 import BeautifulSoup

#baseurl = 'https://hocotech.com/'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

productlinks = []

for x in range (2,4):

	r = requests.get(f'https://hocotech.com/ru/category/звук/наушники/page/{x}/')
	soup = BeautifulSoup(r.content, 'lxml')
	#productlist = soup.find_all('li', class_='isotope-item')
	productlist = soup.find_all('div', class_='desc')	
	for item in productlist:
		for link in item.find_all('a', href=True):
			productlinks.append(link['href'])
		
#print(len(productlinks))

testlink = 'https://hocotech.com/ru/product/звук/наушники/проводные-наушники/m81-imperceptible-проводные-наушники-3-5-mm/'	

r = requests.get(testlink, headers=headers)

soup = BeautifulSoup(r.content, 'lxml')

title = soup.find('h1', class_='product_title').text.strip()

category = soup.select('span > a')[5].text

discription = soup.find('div', class_='woocommerce-product-details__short-description').text.strip()

specification = soup.select('div > p')[3].get_text(strip=True)

print(specification)