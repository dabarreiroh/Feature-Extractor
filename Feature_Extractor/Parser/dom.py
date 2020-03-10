import xml.dom
from lxml import html
import requests



class Dom():
    def __init__(self,html):
        self.html = html

    #def __str__(self):
    #    return str({"forms":str([self.html.forms[i].action for i in range(0,len(self.html.forms))])})

    def formularios(self):
        """
        Function in charge to return the forms found into the url's html. the function receives an html object
        """
        try:
            self.html.forms
        except:
            return {"forms":0}
        else:
            return str({"forms":str([self.html.forms[i].action for i in range(0,len(self.html.forms))])})


    @classmethod
    def Url(cls,url):
        try:
            page = requests.get(url)
            domhtml = html.fromstring(page.content)
        except:
            domhtml={"forms":0}
        return cls(domhtml)

obj=Dom.Url('https://github.com/ecstatic-nobel/OSweep')
print(obj.formularios())