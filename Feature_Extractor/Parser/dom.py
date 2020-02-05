import xml.dom
from lxml import html
import requests



class Dom():
    def __init__(self,html):
        self.html = html

    def __str__(self):
        return str({"forms":str([self.html.forms[i].action for i in range(0,len(self.html.forms))])})

    @classmethod
    def Url(cls,url):
        page = requests.get(url)
        domhtml = html.fromstring(page.content)
        return cls(domhtml)

"""obj=Dom.Url('https://github.com/dabarreiroh/Research-CTAC/blob/master/frame/dom.py')
print(obj)"""