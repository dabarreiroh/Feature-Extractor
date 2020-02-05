#FEATURE-EXTRACTOR#
import Feature_Extractor

urls=open('url.txt')
json=open('jsonresponse.txt','w')

for linea in urls:
 json.write(Feature_Extractor.main(linea))