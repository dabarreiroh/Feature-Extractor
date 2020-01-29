import xml.dom
from lxml import html
import json
import requests



class Dom():
    def __init__(self,html):
        self.html = html
    @classmethod
    def Url(cls,url):
        page = requests.get(url)
        cls.html = html.fromstring(page.content)
        return cls.html
    def __str__(self):
        return 1#json.dumps({"forms":self.html})

obj=Dom.Url('https://facebook.com')
print(obj)