import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.00; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecho) Chrome/106.0.0.0 Safari/537.36'
    'Accept-Language': 'en-US, en;q= 0.5'
}

def get_product_details(product_url: str) -> dict:
    product_details = {}

    page = requests.get(product_url, headers = header)
    soup = BeautifulSoup(page.content, features = 'lxml')
    
    #extracting title and price from html from page
    title = soup.find('span', attrs={'id': 'productTitle'}).get_text().strip()
    price = soup.find('span', attrs={'class': 'a-price'}).get_text().strip() 

    #splitting extracted price to get the correct price
    extracted_price = soup.find('span', attrs = {'class': ' aprice'}).get_text().strip()
    price = '$' + extracted_price.split('$')[1]


    #storing product details into dicitonary
    product_details['title'] = title
    product_details['price'] = price
    product_details['producturl'] = product_url

    return product_details
    except Exception as e:
        print('Could not fetch with product details')
        print(f'Failed with exception: {e}')