import requests 
ses = requests.Session()
from bs4 import BeautifulSoup as parser
class browser:
    def __init__(self,kuki):
        self.kuki = {"cookie":kuki}
    def get(self,link):
        return parser(ses.get("https://mobile.facebook.com" + link,cookies=self.kuki).content,"html.parser")
