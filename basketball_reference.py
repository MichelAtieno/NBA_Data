import requests 

years = list(range(1991,2023))

url_start = "https://www.basketball-reference.com/awards/awards_{}.html"

for year in years:
    url = url_start.format(year)
    data = requests.get(url)
    with open("mvps/{}.html".format(year), "w+") as f:
        f.write(data.text)


