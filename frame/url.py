from functools import wraps
from urllib.parse import urlparse

#decorator
def url_verify(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if 'http' in args[0].url:
            return f(*args, **kwargs)
        else:
            return f(URL('http://NaN/'))#raise RuntimeError('It is not a URL')
    return decorator


class URL:
    """Class to extrac the domain name and url's path from an url"""


    def __init__(self, url):
        self.url = url
        self.domain, self.path = self.analyze_url()

    @url_verify
    def analyze_url(self):
        """
        The funtion analize_url returns the domain name and the url's path from a url.
        This function takes the inner variable url to extract the domain and url's path
        There no need to spicifies an url format
        """

        obj_url = urlparse(self.url)
        dom = obj_url.hostname
        paths = obj_url.path.rsplit('/',obj_url.path.count('/'))[1:]
        if not paths:
            paths=["NaN"]
        for i in range(0, 10):
            try:
                if paths[i] == "":
                    paths[i]= "NaN"
            except:
                paths.insert(i, "NaN")
        return dom, paths


#url = URL(url="http://json.parser.online.fr/")
#url
