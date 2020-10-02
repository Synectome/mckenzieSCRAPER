import os
import requests
import urllib
import http.cookiejar as cookiejar
from bs4 import BeautifulSoup as Beaut
from fake_useragent import UserAgent
from Auction import Auction
from Item import Item
import time
import json


def deco_head():
    print('''    ###########################################
    ###########################################
    ########   Scraping nHentai.net   #########
    ###########################################
    ###########################################
                      V0.1''')


def new_agent():
    ua = UserAgent()
    return str(ua.random)


def load_html(url, with_cookies=False, headers={}):
    """Attempts to load an HTML page, returning a BeautifulSoup instance. Raises
    any networking or parsing exceptions"""
    if with_cookies:
        cj = cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    else:
        opener = urllib.request.build_opener()
    request = urllib.request.Request(url, headers=headers)
    x = True
    count = 1
    while x:
        try:
            response = opener.open(request)
            x = False
            break
        except (urllib.error.HTTPError, ConnectionResetError):
            print("404 in load html")
            count += 1
            if count > 5:
                return None
            time.sleep(count*count)

    html = response.read().decode('utf-8', errors='replace')
    the_soup = Beaut(html, 'html.parser')
    return the_soup


def directory_maker(dir_name):
    print("'")
    cwd = os.getcwd()
    new_directory = os.path.join(cwd, 'auctions')
    if not os.path.exists(new_directory): # check if it exists already
        os.mkdir(new_directory)
    new_directory = os.path.join(new_directory, str(dir_name))
    if not os.path.exists(new_directory):
        os.mkdir(new_directory)
    return new_directory


def find_auction_links(soup):
    # grab the main table containing the auction list
    try:
        container = soup.find('table', id='auction-list')
    except AttributeError:
        return False
    print("we found the auction list!")
    try:
        container = container.find_all("div", class_="panel-title text-nowrap")
    except AttributeError:
        return False
    print("we've got the list of panel divs containing tags")
    print("There are : " + str(len(container)) + " of them.")
    return container


def main():
    deco_head()
    url = 'https://mckenzieauction.hibid.com/'
    auctions_page = url + 'auctions'

    # start the soup
    headers = {'User-Agent': new_agent()}
    soup = load_html(auctions_page, with_cookies=True, headers=headers)
    auction_links = find_auction_links(soup)
    auction_list = []
    for taggroup in auction_links:
        link = taggroup.find("a")
        name = link.text
        link = url+link['href']
        current_auction = Auction(name, len(auction_list)+1, link)
        auction_list.append(current_auction)
    print(auction_list)


if __name__ == "__main__":
    main()