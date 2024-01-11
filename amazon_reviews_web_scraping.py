from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://www.amazon.com/New-Apple-AirPods-Max-Green/dp/B08PZDSP2Z/ref=sr_1_1_sspa?crid=1N93JARQ22ZTM&keywords=airpod%2Bmax&qid=1704414733&sprefix=airpod%2Bmax%2Caps%2C115&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.2b70bf2b-6730-4ccf-ab97-eb60747b8daf&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

reviewers = soup.findAll("span", attrs={"class":"a-profile-name"})

for r in reviewers:
    print(r.text)