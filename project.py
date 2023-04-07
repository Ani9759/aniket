import requests
from bs4 import BeautifulSoup
import csv

# Define the website URL to scrape
url = 'https://www.lifestylestores.com/in/en/storelocator'

# Send a GET request to the website and extract the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the store location details on the page
store_locations = soup.find_all('div', class_='store-list-info')

# Create a list to store the extracted data
store_data = []

# Loop through each store location and extract the required information
for location in store_locations:
    store_name = location.find('div', class_='store-listing-title').text
    store_address = location.find('div', class_='store-listing-address').text.strip()
    store_timings = location.find('div', class_='store-listing-time').text.strip()
    store_phone = location.find('div', class_='store-listing-phone').text.strip()
    store_latitude = location.find('div', class_='store-listing-map')['data-latitude']
    store_longitude = location.find('div', class_='store-listing-map')['data-longitude']

    # Create a dictionary to store the extracted data
    store = {
        'store_name': store_name,
        'store_address': store_address,
        'store_timings': store_timings,
        'store_phone': store_phone,
        'store_latitude': store_latitude,
        'store_longitude': store_longitude
    }
    store_data.append(store)

# Write the extracted data to a CSV file
with open('lifestyle_store_locations.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['store_name', 'store_address', 'store_timings', 'store_phone', 'store_latitude', 'store_longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for store in store_data:
        writer.writerow(store)

