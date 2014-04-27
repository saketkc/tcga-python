#!/usr/bin/env python
import requests
import unittest
from bs4 import BeautifulSoup
__tcga_url__ = 'http://tcga-data.nci.nih.gov/tcgadccws/Get'


class TCGADownloader():

    def __init__(self, url=__tcga_url__):
        self.url = url

    def make_query(self, retrieval_format, params):
        """Makes a GET request with the passed in parameters for
        XML/HTML retrieval format
        """
        assert retrieval_format in ['XML', 'HTML']
        url = self.url + retrieval_format
        request = requests.get(url, params=params)
        return request

    def get_diseases(self):
        """Get all diseases"""
        query = self.make_query('XML', {'query': 'Disease'})


    def get_soup(self, response):
        soup = BeautifulSoup(response)
        return soup


class TCGADownloaderTestFunctions(unittest.TestCase):

    def setUp(self):
        self.downloader = TCGADownloader()

    def test_get_diseases(self):
        query = self.downloader.get_diseases()
        soup = self.downloader.get_soup(query.text)
        print soup
        self.assertEqual(query.status_code, 200)


if __name__ == '__main__':
    suite = unittest.TestLoader()\
        .loadTestsFromTestCase(TCGADownloaderTestFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
