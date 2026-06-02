import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

for page in range(1, 6):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]

        data.append([title, price, rating])

df = pd.DataFrame(data, columns=["Title", "Price", "Rating"])

df.to_csv("books_market_data.csv", index=False)

print(f"Successfully Scraped {len(df)} Books")