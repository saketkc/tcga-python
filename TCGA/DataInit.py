import requests
from bs4 import BeautifulSoup
__base_url__ = "https://tcga-data.nci.nih.gov/datareports/"
class DataInit:
    def __init__(self,url=__base_url__):
        self.url = url
    def get_homepage_response(self):
        response = requests.get(self.url)
        if response.

