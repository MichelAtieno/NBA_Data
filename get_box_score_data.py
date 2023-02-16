import os, time
from bs4 import BeautifulSoup
import pandas as pd
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
import asyncio
from give_data import DATA_DIR, STANDINGS_DIR, get_html, SEASONS

SCORES_DIR = os.path.join(DATA_DIR, "scores")

standings_files = os.listdir(STANDINGS_DIR)
print(standings_files)
standings_file = os.path.join(STANDINGS_DIR, standings_files[0])

async def scrape_game(standings_file):
    with open(standings_file, 'r') as f:
        html = f.read()

    soup = BeautifulSoup(html, features="lxml")
    links = soup.find_all("a")
    hrefs = [l.get("href") for l in links]
    box_scores = [l for l in hrefs if l and "boxscore" in l and ".html in l"]
    box_scores = [f"https://www.basketball-reference.com{l}" for l in box_scores]
    for url in box_scores:
        save_path = os.path.join(SCORES_DIR, url.split("/")[-1])
        if os.path.exists(save_path):
            continue

        html = await get_html(url, "#content")
        if not html:
            continue
        with open(save_path, "w+") as f:
            f.write(html)

## Filters out any files that are not appropriate
# standings_files = [for s in standings_files if ".html" in s] 

for f in standings_files:
    filepath = os.path.join(STANDINGS_DIR, f)

    asyncio.run(scrape_game(filepath))
