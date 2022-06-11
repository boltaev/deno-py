import requests
from bs4 import BeautifulSoup
from xlwt import Workbook

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 YaBrowser/17.6.1.749 Yowser/2.5 Safari/537.36'
}
filename = 'HOCO_Headphones.xls'


# loop for range every page of site between operands
def count_items(first, last):
    product_links = []
    for x in range(first, last):
        r = requests.get(f'https://hocotech.com/ru/category/звук/наушники/page/{x}/')
        soup = BeautifulSoup(r.content, 'lxml')
        product_list = soup.find_all('div', class_='desc')
        # getting href of every single product from catalog
        for item in product_list:
            for link in item.find_all('a', href=True):
                product_links.append(link['href'])
        print('finish read page: ', x)
    return product_links


# getting data from products page
def get_data(file_name, product_links):
    i = 1
    wb = Workbook()
    amount = len(product_links)
    sheet1 = wb.add_sheet('HOCO')

    for link in product_links:
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        try:
            name = soup.find('h1', class_='product_title').text.strip()
        except:
            name = ''

        try:
            category = soup.find('span', class_='posted_in').text.strip("Категория: ")
        except:
            category = ''

        try:
            description = soup.find('div', class_='woocommerce-product-details__short-description').text.strip()
        except:
            description = ''

        # cannot be worse, look I'm catching third p from entire page
        # text alternative is get_text() function for select function
        try:
            specification = soup.select('div > p')[3].text
        except:
            specification = ''

        product = {
            'name': name,
            'category': category,
            'description': description,
            'specification': specification,
            'url': link
        }
        sheet1.write(i, 1, product['name'])
        sheet1.write(i, 2, product['category'])
        sheet1.write(i, 3, product['description'])
        sheet1.write(i, 4, product['specification'])
        sheet1.write(i, 5, product['url'])
        print(i, '/', amount, ' saving: ', product['name'])
        i += 1
        wb.save(file_name)


products_links = count_items(1, 21)
get_data(filename, products_links)
print('extracted data saved successfully into: ', filename)
