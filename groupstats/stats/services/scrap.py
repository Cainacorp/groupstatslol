import requests
from bs4 import BeautifulSoup
from groupstats.stats.models import Summoner


url_log = 'https://www.leagueofgraphs.com/summoner/las/%s#championsData-flex'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def scrap_single_profile_and_store(summoner: Summoner):
    url = url_log % (summoner.log_scraping_name())
    response = requests.get(url, headers=headers)

    # TODO continuar
