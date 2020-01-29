from functools import wraps
import urllib3
from urllib.parse import urlparse
import json

#decorator
def url_verify(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if 'http' in args[0].url:
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
        self.domain, self.path,self.subdomain = self.analyze_url()





    @url_verify
    def analyze_url(self):
        npaths=self.kwargs["npaths"]
        obj_url = urlparse(self.url)
        sub = obj_url.hostname.rsplit('.', obj_url.hostname.count('.'))[0:1]
        dom = obj_url.hostname.rsplit('.',obj_url.hostname.count('.'))[1:]
        if (sub == dom[0] ):
            sub=""
        else:
            if (len(dom[0])<4):
                dom = obj_url.hostname.rsplit('.', obj_url.hostname.count('.'))[0:]
                sub=""
        sub='.'.join(sub)
        dom='.'.join(dom)
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
        return dom, paths[0:npaths],sub

    def json(self):
        return json.dumps({ "domain":self.domain, "paths":self.path[0:],"subdomain":self.subdomain})
a=URL("https://json.parser.online.fr",npaths='default')
print(a.json())
print(a.path)
print(a.domain)
print(a.subdomain)
