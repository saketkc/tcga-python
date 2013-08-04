import requests
from bs4 import BeautifulSoup
__base_url__ = "https://tcga-data.nci.nih.gov/datareports/"
class DataInit:
    def __init__(self,url=__base_url__):
        self.url = url
    def get_homepage_response(self):
        response = requests.get(self.url)
        if response.ok:
            return response.content
        else:
            raise "Error making a request"
    def make_soup(self,response):
        soup = BeautifulSoup(response)
        return soup
    def get_all_download_urls(self,soup):
        forms = soup.findAll("form",{"name":"csvExport"})
        return forms

    def download_csv(self,forms,download_path):
        for form in forms:
            action = form.attrs["action"]
            filename = action.split("=")[-1]
            with open(download_path+"/"+filename+".csv","w") as filetowrite:
                request= requests.post(__base_url__+"/"+action)
                filetowrite.write(request.content)



if __name__ == "__main__":
    datadownloader = DataInit("https://tcga-data.nci.nih.gov/datareports/codeTablesReport.htm")
    data_response = datadownloader.get_homepage_response()
    #print data_response
    if data_response:
        soup = datadownloader.make_soup(data_response)
        forms = datadownloader.get_all_download_urls(soup)
        download_csv = datadownloader.download_csv(forms,download_path="/home/saket/my-softwares/tcga-python/TCGA/data/")




