import requests 
from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
#baseurl = 'https://hocotech.com/'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 YaBrowser/17.6.1.749 Yowser/2.5 Safari/537.36'
}
productLinks = []

# loop for range every page of site between operands
for x in range (2,3):

	r = requests.get(f'https://hocotech.com/ru/category/звук/наушники/page/{x}/')
	soup = BeautifulSoup(r.content, 'lxml')
	productList = soup.find_all('div', class_='desc')
	# getting href of every single product from catalog
	for item in productList:
		for link in item.find_all('a', href=True):
			productLinks.append(link['href'])
	print('finish read page: ', x)		
		
amount = len(productLinks)
#elementList = []
i = 1
wb = Workbook()
sheet1 = wb.add_sheet('hoco')
# getting data from products page
for link in productLinks:
	r = requests.get(link, headers=headers)
	soup = BeautifulSoup(r.content, 'lxml')
	name = soup.find('h1', class_='product_title').text.strip()
	category = soup.find('span', class_='posted_in').text.strip("Категория: ")
	description = soup.find('div', class_='woocommerce-product-details__short-description').text.strip()
	
	#cannot be worse, look I'm catching third p from entire page
	# text alternative is get_text() function for select function
	specification = soup.select('div > p')[3].text
	product = {
		'name': name,
		'category': category,
		'description': description,
		'specification': specification,
		'url': link
	}
	#elementList.append(product)
	sheet1.write(i, 1, product['name'])
	sheet1.write(i, 2, product['category'])
	sheet1.write(i, 3, product['description'])
	sheet1.write(i, 4, product['specification'])
	sheet1.write(i, 5, product['url'])
	print(i, '/', amount, ' saving: ', product['name'])
	i += 1
	wb.save('sample_data2.xls')
print('saved successfully')