import requests
from bs4 import BeautifulSoup

url = "https://www.dataroma.com/m/home.php"

# Define custom headers to mimic a web browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
}

response = requests.get(url, headers=headers)

# Check the HTTP status code to ensure the connection was successful
if response.status_code == 200:
    print("Connection successful (status code 200)")

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the <table> elements on the webpage
    tables = soup.find_all('table')

    # Loop through each table to extract and print its data
    for table in tables:
        # Find all the <tr> elements (table rows) within the table
        rows = table.find_all('tr')

        # Loop through the rows to extract data
        for row in rows:
            # Extract data from each row as needed
            columns = row.find_all('td')
            for column in columns:
                # Get the text within the <td> element
                data = column.get_text(strip=True)
                print(data)
else:
    print(f"Failed to connect to the website. Status code: {response.status_code}")
