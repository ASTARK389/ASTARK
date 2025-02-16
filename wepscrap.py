# web sraping
import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://www.sarkariresult.com/"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract specific data (e.g., all headings)
headings = soup.find_all("h1")
for heading in headings:
    print(heading.text)