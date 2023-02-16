import os, time
from bs4 import BeautifulSoup
import pandas as pd
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
import asyncio

SEASONS = list(range(2016, 2023))
print(SEASONS)

DATA_DIR = "data2"
STANDINGS_DIR = os.path.join(DATA_DIR, "standings")

async def get_html(url, selector, sleep=5, retries=3):
    html = None
    for i in range(1, retries+1):
        time.sleep(sleep * i)

        try:
            async with async_playwright() as p:
                browser = await p.firefox.launch()
                page = await browser.new_page()
                await page.goto(url)
                print(await page.title())
                html = await page.inner_html(selector)
        except PlaywrightTimeout:
            print(f"Timeout error on {url}")
            continue
        else:
            break
    return html

async def scrape_season(season):
    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_games.html"
    html = await get_html(url, "#content .filter")
    soup = BeautifulSoup(html, features="lxml")
    links = soup.find_all("a")
    href = [l["href"] for l in links]
    standings_pages = [f"https://www.basketball-reference.com{l}" for l in href]
    for url in standings_pages:
        save_path = os.path.join(STANDINGS_DIR, url.split("/")[-1])
        if os.path.exists(save_path):
            continue

        html = await get_html(url, "#all_schedule")
        with open(save_path, "w+") as f:
            f.write(html)

for season in SEASONS:
    asyncio.run(scrape_season(season))

# season = 2016
# url = f"https://www.basketball-reference.com/leagues/NBA_{season}_games.html"
# html = asyncio.run(get_html(url, "#content .filter"))

# # print(html)

# soup = BeautifulSoup(html, features="lxml")
# links = soup.find_all("a")
# href = [l["href"] for l in links]
# standings_pages = [f"https://www.basketball-reference.com{l}" for l in href]
# print(href)