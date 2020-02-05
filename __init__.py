#FEATURE-EXTRACTOR#
import Feature_Extractor
import json
from io import open
result={}
urls=open('url.txt','r')
#urls.readlines()
jsonresponse=open('jsonresponse.txt','w')
count=0
for linea in urls.readlines():
    result.update({count:Feature_Extractor.main(linea.replace('\n','')).whois}) 
    count+=1
jsonresponse.write(json.dumps(result))