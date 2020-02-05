"""
Module to find the whois record
"""


import json
from Feature_Extractor.Extractor import parse_response
from Feature_Extractor.Extractor import whois_query
from Feature_Extractor.Extractor import ssl_cert
from Feature_Extractor.Parser import url_parser
from Feature_Extractor.Parser import dom

#Procedure to extract all the whois information through the whois and dig linux command
#
# Find the domain name
# Find the registrar whois server
# Find IP address
# Find whois related to IP address
# Retrive a Json with information gathered

class main(): 

    def __init__(self,url):
        self.whois(url)

    def whois(self,url):
        """
        Method to return the whois information relate to the an url.
        Procedure:
        1.Find the domain name
        2. Find the registrar whois server
        3. Find IP address
        4. Find whois related to IP address
        5. Retrive a Json with information gathered
        """
        


        urlw = url_parser.URL(url)
        wh = whois_query.Whois()
        data = wh.whois(dom = urlw.domain)
        certificate = ssl_cert.ssl_certificate(urlw.domain)
        
        domain = dom.Dom.Url(url)

        dicc1 = parse_response.jsonparser(data=data['w'],dict={},keyword='Domain Whois Record')
        dicc2 = parse_response.jsonparser(data=data['w_server'],dict=dicc1,keyword='Registrar Whois Record')
        dicc3 = parse_response.jsonparser(data=data['w_ip'],dict=dicc2,keyword='Network Whois Record')
        dicc3['Address Lookup'] = data['ip'].split('\n')
        dicc3['SSL Certificate'] = certificate
        dicc3['Html Info'] = {"forms":str([domain.html.forms[i].action for i in range(0,len(domain.html.forms))])}

        json_response = json.dumps(dicc3)
        print(json_response)

        
       
            
        
    









test =  main('https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse')








