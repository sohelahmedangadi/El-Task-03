import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("h2")

    print(headlines)

    with open("headlines.txt", "w", encoding="utf-8") as f:
        count = 1
        for headline in headlines:
            text = headline.get_text(strip=True)

            if text:
                print(f"{count}. {text}")
                f.write(f"{count}. {text}\n")
                count += 1

    print("\nHeadlines saved successfully!")

else:
    print("Failed to fetch webpage")
