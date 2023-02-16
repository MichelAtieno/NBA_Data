import requests
from bs4 import BeautifulSoup
import pandas as pd

with open("mvps/1991.html") as f:
    page = f.read()

soup = BeautifulSoup(page, "html.parser")
print(soup.find("tr", class_="over_header").decompose())
mvp_table = soup.find(id="mvp")
print(mvp_table)

mvp_1991 = pd.read_html(str(mvp_table))
print(mvp_1991)

years = list(range(1991,2023))

# dfs = []
# for year in years:
#     with open("mvps/{}.html".format(year)) as f:
#         page = f.read()
#         soup = BeautifulSoup(page, "html.parser")
#         soup.find("tr", class_="over_header").decompose()
#         mvp_table = soup.find(id="mvp")
#         mvp = pd.read_html(str(mvp_table))

#         dfs.append(mvp)

# print(dfs)