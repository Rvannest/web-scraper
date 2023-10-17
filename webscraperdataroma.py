import requests
from bs4 import BeautifulSoup

url = "https://www.dataroma.com/m/home.php"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Find the parent <tr> element that contains the tables
table_row = soup.find('tr')

if table_row:
    # Find all the <td> elements (table cells) within the parent <tr>
    table_cells = table_row.find_all('td')

    # Loop through each <td> (table cell) to process its data
    for cell in table_cells:
        # Extract and print the data within each <a> element
        links = cell.find_all('a')
        for link in links:
            # Get the text within the <a> element
            stock_data = link.get_text(strip=True)
            print(stock_data)
else:
    print("Table row not found. Check the HTML structure.")
