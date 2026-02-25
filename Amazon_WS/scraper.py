import requests
from bs4 import beautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.00; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecho) Chrome/106.0.0.0 Safari/537.36'
    'Accept-Language': 'en-US, en;q= 0.5'
}

def get_product_details(product_url: str) -> dict:
    product_details = {}

    page = requests.get(product_url, headers = header)
    soup = BeautifulSoup(page.content, features = 'lxml')

    