#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 19:25:03 2018

@author: jinzhao
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

# Set up
file = open('NBA_2017.txt', 'w')
file.truncate()
file.close()

# Scraping
urls = [
"https://www.basketball-reference.com/leagues/NBA_2018_games.html",
"https://www.basketball-reference.com/leagues/NBA_2018_games-november.html",
"https://www.basketball-reference.com/leagues/NBA_2018_games-december.html",
"https://www.basketball-reference.com/leagues/NBA_2018_games-january.html",
"https://www.basketball-reference.com/leagues/NBA_2018_games-february.html",
"https://www.basketball-reference.com/leagues/NBA_2018_games-march.html",
"https://www.basketball-reference.com/leagues/NBA_2018_games-april.html",
]

for url in urls:
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    parent = soup.tbody
    with open('NBA_2017.txt', 'a') as file:
        for child in parent.contents:
            if child.name == None:
                continue
            else:
                if child.contents[2:6] == []:
                    break
                for grand_child in child.contents[2:6]:
                    file.write(grand_child.string)
                    file.write('\n')
    file.close()

