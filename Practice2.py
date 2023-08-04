# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.sharekhan.com/market/market-research"
# headers = {"Accept": "*/*", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
# webPage = requests.get(url, headers=headers)
# soup = BeautifulSoup(webPage.content, "html.parser")
#
# divs_with_specific_class = soup.find_all("div", class_="dataTables_sizing")
# for div in divs_with_specific_class:
#     print(div.text)
# div_with_specific_id = soup.find("div", id="DataTables_Table_0")
# if div_with_specific_id:
#     print(div_with_specific_id.text)