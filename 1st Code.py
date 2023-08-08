# '''import requests
# from bs4 import BeautifulSoup
# url="https://www.cnbc.com/world/?region=world"
# x=requests.get(url)
# print(x.text)
#
# soup=BeautifulSoup(x.content,"html.parser")
# print(soup.text)
#
# # images
# image=soup.findAll('dev',class_='imgTagWrapper')
# # print(image)
# image1=[]
# for i in image:
#     j=i.img['scr']
#     # print(j)
#     image1.append(j)
# print(image1)'''
#
#
#
import requests
from bs4 import BeautifulSoup
"""import json
def scrape_analyst_recommendations(stock_symbol):
    url = "https://www.investing.com/equities/{stock_symbol}-recommendations"
    # Send a GET request to the URL
    response = requests.get(url)
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the table that contains the analyst recommendations
    table = soup.find('table', class_='genTbl')
    # Find all rows in the table (excluding the header row)
    rows = table.find_all('tr')[0:]
    recommendations = []
    # Iterate over each row and extract the relevant data
    for row in rows:
        columns = row.find_all('td')
        date = columns[0].text.strip()
        rating = columns[1].text.strip()
        analyst = columns[2].text.strip()
        # Store the recommendation data in a dictionary
        recommendation = {
            'Date': date,
            'Rating': rating,
            'Analyst': analyst
        }
        recommendations.append(recommendation)
    return recommendations
# Usage example: Scrape analyst recommendations for Reliance Industries (RELIANCE.NS)
recommendations = scrape_analyst_recommendations('Reliance Industries')
for recommendation in recommendations:
    print(recommendation)
abc=json.dumps(recommendation)
print(type(abc))"""



# Import requests and BeautifulSoup libraries
"""import requests
from bs4 import BeautifulSoup
import json
# Define the url
url = "https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT"

# Send a GET request and get the response
response = requests.get(url)

# Parse the response using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find the div element that contains the BROKER RESEARCH data
div = soup.find("div", id="broker_research")

# Find all the tr elements inside the div
trs = div.find_all("tr")

# Create an empty list to store the data
data = []

# Loop through each tr element
for tr in trs:
    # Find all the td elements inside the tr
    tds = tr.find_all("td")
    # Create an empty list to store the row data
    row = []
    # Loop through each td element
    for td in tds:
        # Get the text content of the td and strip any whitespace
        text = td.text.strip()
        # Append the text to the row list
        row.append(text)
    # Append the row list to the data list
    data.append(row)

# Print the data list
print(data)
abc=json.dumps(data)
print(type(abc))
"""



# import requests
# from bs4 import BeautifulSoup
# url="https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT"
# x=requests.get(url)
# print(x.text)
#
# soup=BeautifulSoup(x.content,"html.parser")
# print(soup.text)
# # broker name
# Name=soup.findAll('dev',class_='brstk_name')
# # print(image)
# broker=[]
# for i in Name:
#     j=i.nam['scr']
#     print(j)
#     broker.append(j)
# print(broker)
# import requests
# from bs4 import BeautifulSoup
#
# def get_broker_research_data(url):
#   """
#   Gets the data of BROKER RESEARCH from the given URL.
#
#   Args:
#     url: The URL of the page containing the BROKER RESEARCH data.
#
#   Returns:
#     A list of dictionaries containing the BROKER RESEARCH data.
#   """
#
#   response = requests.get(url)
#   soup = BeautifulSoup(response.content, 'html.parser')
#
#   broker_research_data = []
#   for div in soup.find_all('div', class_='mc-res-itm'):
#     broker_name, exchange_rate, date, reco_price, target_price = (
#         div.find('a', class_='mc-res-tit').text.strip(),
#         div.find('span', class_='mc-res-exch').text.strip(),
#         div.find('span', class_='mc-res-dt').text.strip(),
#         div.find('span', class_='mc-res-val').text.strip(),
#         div.find('span', class_='mc-res-tgt').text.strip(),
#     )
#
#     broker_research_data.append({
#       'broker_name': broker_name,
#       'exchange_rate': exchange_rate,
#       'date': date,
#       'reco_price': reco_price,
#       'target_price': target_price,
#     })
#
#   return broker_research_data
#
#
# def main():
#   """
#   Main function.
#
#   Gets the data of BROKER RESEARCH from the given URL and prints it to the console.
#   """
#
#   url = 'https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT'
#   broker_research_data = get_broker_research_data(url)
#
#   for broker_research in broker_research_data:
#     print(broker_research)
#
#
# if __name__ == '__main__':
#   main()



import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def scrape_analyst_recommendations(time_period):
    url = "https://www.investing.com/stock-screener/Service/SearchStocks"

    # Define the payload parameters for the POST request
    payload = {
        'country[]': '3',
        'exchange[]': '50',
        'sector': '0',
        'industry': '0',
        'pn': '1',
        'order[col]': 'name',
        'order[dir]': 'a'
    }

    # Send a POST request to retrieve the stock list
    response = requests.post(url, data=payload)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table that contains the stock list
    table = soup.find('table', id='resultsTable')

    # Find all rows in the table (excluding the header row)
    rows = table.find_all('tr')[1:]  # Start from index 1 to skip the header row

    recommendations = []

    # Iterate over each row to scrape analyst recommendations for each stock
#     for row in rows:
#         symbol = row.find('a')['href'].split('/')[-1]
#         stock_name = row.find('a').text.strip()
#
#         # Create the URL for the analyst recommendations of the stock
#         recommendations_url = f"https://www.investing.com/equities/{symbol}-recommendations"
#
#         # Send a GET request to the URL
#         response = requests.get(recommendations_url)
#
#         # Create a BeautifulSoup object to parse the HTML content
#         soup = BeautifulSoup(response.content, 'html.parser')
#
#         # Find the table that contains the analyst recommendations
#         table = soup.find('table', class_='recommendationsByCompany')
#
#         if table:
#             # Find all rows in the table (excluding the header row)
#             rows = table.find_all('tr')[1:]  # Start from index 1 to skip the header row
#
#             # Iterate over each row and extract the relevant data for yesterday's recommendations
#             for row in rows:
#                 columns = row.find_all('td')
#                 date = columns[0].text.strip()
#                 rating = columns[1].text.strip()
#                 analyst = columns[2].text.strip()
#
#                 # Check if the recommendation is from yesterday
#                 recommendation_date = datetime.strptime(date, '%b %d, %Y')
#                 yesterday = datetime.now() - timedelta(days=1)
#
#                 if recommendation_date.date() == yesterday.date():
#                     # Store the recommendation data in a dictionary
#                     recommendation = {
#                         'Symbol': symbol,
#                         'Stock Name': stock_name,
#                         'Date': date,
#                         'Rating': rating,
#                         'Analyst': analyst
#                     }
#
#                     recommendations.append(recommendation)
#
#     return recommendations
#
#
# # Usage example: Scrape analyst recommendations for all stocks listed on NSE from yesterday
# recommendations = scrape_analyst_recommendations('day1')
# for recommendation in recommendations:
#     print(recommendation)





















