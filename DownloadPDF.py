###########################################
#
# Script to scrap and download pdf
# from https://ww2.nycourts.gov/courts/2jd/kings/civil/foreclosuresales.shtml
# Code by Shiyu Hu
#
##########################################

# import library
import requests
from bs4 import BeautifulSoup

###################
# Get the target url List of Properties
###################
url_origin = "https://ww2.nycourts.gov/courts/2jd/kings/civil/foreclosuresales.shtml"
request_1 = requests.get(url_origin)
soup = BeautifulSoup(request_1.text, "html.parser")

url = ""
for link in soup.find_all('a', string = "LIST OF PROPERTIES"):
    url = link['href']
    print(url)

###################
# scrape PDF documents from target url(List of Properties)
###################
# make HTTP to GET requests to the target URL (List of Properties)
response = requests.get(url)
# parse content
soup = BeautifulSoup(response.text, "html.parser")
# Find all links present on a webpage
links = soup.find_all("a")
i = 0
# Check the pdf links in all the links and if present download file
# Requests URL and get response object
for link in links:
    if ".pdf" in link.get('href'):
        i += 1
        print("Downloading....", i)
        link = "https://www.nycourts.gov" + link['href']
        # Get response for each link
        response = requests.get(link)
        # Download PDF
        pdf = open("pdf" + str(i) + ".pdf", "wb")
        pdf.write(response.content)
        pdf.close()
        print("PDF file", i, "downloaded")
print("All PDF files downloaded")







