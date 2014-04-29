#!/usr/bin/env python
import requests
import unittest
from bs4 import BeautifulSoup
__dccws_url__ = 'http://tcga-data.nci.nih.gov/tcgadccws/Get'
__datamatrix_url__ = 'http://tcga-data.nci.nih.gov/tcga/damws/jobprocess'


class TCGADownloader():

    def __init__(self, url=__dccws_url__):
        self.url = url
        self.query = None

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
        self.query = self.make_query('XML', {'query': 'Disease'})
        return self.query

    def get_platforms(self):
        self.query = self.make_query('XML', {'query': 'Platform'})
        return self.query

    def get_center_list(self):
        self.query = self.make_query('XML', {'query': 'Center'})
        return self.query

    def parse_fields(self, fields):
        response = {}
        for field in fields:
            try:
                response[field['name']] = field['xlink:href']
            except KeyError:
                response[field['name']] = field.string
        return response

    def get_classes_from_xml(self):
        soup = self.get_soup()
        classes = soup.findAll('class')
        print classes[1]
        for record in classes:
            try:
                recordnumber = record['recordnumber']
                fields = record.findAll('field')
                print self.parse_fields(fields)
            except KeyError:
                pass
        return classes

    def get_soup(self):
        soup = BeautifulSoup(self.query.text)
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
    #suite = unittest.TestLoader()\
     #   .loadTestsFromTestCase(TCGADownloaderTestFunctions)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    downloader = TCGADownloader()
    platforms = downloader.get_platforms()
    centers = downloader.get_center_list().text
    print centers
    downloader.get_classes_from_xml()
