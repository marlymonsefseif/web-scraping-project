import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.amazon.eg/s?k=apple+airpods&i=electronics&bbn=18018102031&rh=n%3A18018102031%2Cp_89%3ASony&dc&language=en'
page = requests.get(url)
# print(page.content)
soup = BeautifulSoup(page.content, "html.parser")

nameProduct = []
price = []
shipping = []
review = []
rating = []

name_product = soup.find_all('span', {'class': 'a-size-base-plus a-color-base a-text-normal'})
cost = soup.find_all('span', {'class': 'a-price-whole'})
ship_product = soup.find_all('div', {'class': 'a-row a-size-base a-color-secondary s-align-children-center'})
review_product = soup.find_all('span', {'class': 'a-size-base s-underline-text'})
rate_product = soup.find_all('span', {'class': 'a-icon-alt'})


for i in range(len(rate_product)):
    rating.append(rate_product[i].text)
for i in range(len(name_product)):
    nameProduct.append(name_product[i].text)
for i in range(len(cost)):
    price.append(cost[i].text)
for i in range(len(review_product)):
    review.append(review_product[i].text)
for i in range(len(ship_product)):
    shipping.append(ship_product[i].text)

'''
for i in range(len(cost)):
    nameProduct.append(name_product[i].text)
    price.append(cost[i].text)
    shipping.append(ship_product[i].text)
    review.append(review_product[i].text)
    rating.append(rate_product[i].text)
'''

dict_product = {'Product Name': nameProduct, 'Price': price, 'Shipping and Time': shipping, 'Rating': rating, 'Review': review}
# print(len(nameProduct), len(price), len(shipping), len(rating), len(review))

df = pd.DataFrame.from_dict(dict_product, orient='index')
df.dropna(axis=1, inplace=True)

prod_reviews = df.T

prod_reviews.to_csv('amazon.csv', index=False, header=True)
