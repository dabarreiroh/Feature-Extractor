import xml.dom
from lxml import html
import json
import requests



class Dom():
    def __init__(self,html):
        self.html = html

    def __str__(self):
        return json.dumps({"forms":str([self.html.forms[i].action for i in range(0,len(self.html.forms))])})

    @classmethod
    def Url(cls,url):
        page = requests.get(url)
        domhtml = html.fromstring(page.content)
        return cls(domhtml)

obj=Dom.Url('https://facebook.com')
print(obj)