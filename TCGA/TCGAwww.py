#!/usr/bin/env python
import requests
__tcga_url__ = "http://tcga-data.nci.nih.gov/tcgadccws/Get"
class TCGADownloader():

    def __init__( self, url=__tcga_url__, retrieval_format="XML" ):
        self.url = url
        assert retrieval_format in ["XML", "HTML"]
        self.retrieval_format = retrieval_format

    def  make_query( query_term=None):
        params = {}
        self.request = requests.get(self.url, )




