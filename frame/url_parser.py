from functools import wraps
import urllib3
from urllib.parse import urlparse
import json
import threading
import re

#decorator
#def url_verify(f):
#    @wraps(f)
#    def decorator(*args, **kwargs):
#        if 'http' in args[0].url:
#            return f(*args, **kwargs)
#        else:
#            #return f(URL('http://NaN/',npaths=10))#raise RuntimeError('It is not a URL')
#            return f(URL('http://'+args[0].url,npaths=10))#raise RuntimeError('It is not a URL')
#    return decorator

def url_verify(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        match = re.search(r'(http.?)?(://)+([\._\-~a-zA-Z0-9\.]{1,}).([:0-9]{0,})|(ftp)?(://)+([\._\-~a-zA-Z0-9\.]{1,}).([:0-9]{0,})',args[0].url)
        url_main2 = args[0].url.split('/')
        url_main = "/".join(url_main2[0:3])
        if len(match.group()) == len(url_main):
            return f(*args, **kwargs)
        else:
            return f(URL('http://NaN/',npaths=10))#raise RuntimeError('It is not a URL')
    return decorator

class URL:

    def __init__(self, url,**kwargs):
        self.url = url
        if not kwargs:
            kwargs = {"npaths": 10}
        self.kwargs = kwargs
        self.domain, self.path, self.subdomain, self.url_body  = self.analyze_url()


    @url_verify
    def analyze_url(self):
        npaths=self.kwargs["npaths"]
        obj_url = urlparse(self.url)
        #sub = obj_url.hostname.rsplit('.', obj_url.hostname.count('.'))[0:1]
        url_body = obj_url.hostname 
        dom = obj_url.hostname.rsplit('.',obj_url.hostname.count('.'))[-2:]
        if (len(dom[0])<4):
            dom = obj_url.hostname.rsplit('.', obj_url.hostname.count('.'))[-3:]
            sub=obj_url.hostname.replace('.'.join(dom),'')
        dom='.'.join(dom)
        sub = obj_url.hostname.replace('.'+dom, '')
        paths = obj_url.path.rsplit('/',obj_url.path.count('/'))[1:]
        #self.url.replace(obj_url.hostname,'').replace('https','').replace('http','').replace('/','').replace(obj_url.path,'')
        if npaths == 'default':
            npaths=len(paths)
        if not paths:
            paths=["NaN"]
        for i in range(0, npaths):
            try:
                if paths[i] == "":
                    paths[i]= "NaN"
            except:
                paths.insert (i, "NaN")
        return dom, paths[0:npaths],sub,url_body



    def json(self):
        return json.dumps({ "domain":self.domain, "paths":self.path[0:],"subdomain":self.subdomain, "url_body":self.url_body })




a=URL('ftp://f4tg_.fo.c-o_m.rar:4846/aaasdf@#asdgg/asdgsg/s',npaths='default')
print(a.json())
print(a.path)
print(a.domain)
print(a.subdomain)