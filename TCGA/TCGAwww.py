#!/usr/bin/env python
import requests
import unittest
__tcga_url__ = 'http://tcga-data.nci.nih.gov/tcgadccws/Get'
class TCGADownloader():

    def __init__(self, url=__tcga_url__):
        self.url = url

    def make_query(retrieval_format, params):
        assert retrieval_format in ['XML', 'HTML']
        url = self.url + retrieval_format
        request = requests.get(url, params=params)
        response = request.text
        return response

    def get_diseases():
        return make_query('XML', {'query': Diseases})


class TCGADownloaderTestFunctions(unittests):
    def setUP(self):
        self.setup = TCGADownloader()

    def test_make_query(self):
        query = make_query()
