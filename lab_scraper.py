import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_labuncle_data():
    data = []

    lab_urls = [
        "https://www.labuncle.com/packages/good-health-package-1433",
        "https://www.labuncle.com/packages/health-champion-radiology-package-1677",
    ]

    for url in lab_urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')


        lab_name = soup.find("h1", class_="page-title").text.strip()
        test_name = soup.find("div", class_="test-name").text.strip()
        test_price = soup.find("span", class_="price").text.strip()

        data.append([lab_name, test_name, test_price, url])

    # Create DataFrame and save to CSV
    df = pd.DataFrame(data, columns=["Lab Name", "Test Name", "Test Price", "URL"])
    df.to_csv("labuncle_data.csv", index=False)


scrape_labuncle_data()