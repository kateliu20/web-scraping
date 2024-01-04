from bs4 import BeautifulSoup
import requests

# very simple web scraping script
# directly from online tutorial: https://www.youtube.com/watch?v=QhD015WUMxE

page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

for quote in quotes:
    print(quote.text)

for author in authors:
    print(author.text)