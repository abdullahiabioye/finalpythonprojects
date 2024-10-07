import requests
from bs4 import BeautifulSoup

url = 'https://www.aljazeera.com/' 

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all('h1')  

print("WebScraper Scraped:")
for title in titles:
    print(title.get_text(strip=True))































































# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # Function to extract data from a single page
# def extract_data_from_page(url):
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')

#     # Modify these based on the website structure
#     titles = soup.find_all('h2', class_='entry-title')
#     data_list = []

#     for title in titles:
#         link = title.find('a')['href']
#         text = title.get_text(strip=True)
#         data_list.append({'Title': text, 'URL': link})
    
#     return data_list

# # Function to handle pagination
# def scrape_paginated_website(base_url, num_pages):
#     all_data = []

#     for page_num in range(1, num_pages + 1):
#         # Modify this part based on the URL structure of pagination
#         paginated_url = f"{base_url}/page/{page_num}/"
#         print(f"Scraping page: {paginated_url}")
#         page_data = extract_data_from_page(paginated_url)
#         all_data.extend(page_data)

#     return all_data

# # Define the base URL and number of pages to scrape
# base_url = 'https://example.com/articles'  # Example website
# num_pages = 5  # Number of pages to scrape

# # Scrape data from the paginated website
# scraped_data = scrape_paginated_website(base_url, num_pages)

# # Store the data in a CSV file
# df = pd.DataFrame(scraped_data)
# df.to_csv('extrac.csv', index=False)
# print("Data has been written to extrac.csv")
