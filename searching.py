# script to crawl website

import urllib.request
import re
baseurl="https://www.bing.com/search?q="
oquery="what is the capital of india"
squery= oquery.replace(' ', '+')
query = baseurl+squery
#print(query)
url= urllib.request.urlopen(query)
data=url.read()
data=str(data)
#regex= "href=\".*?\""
#p=re.compile(regex)
#s= re.findall(r'href=\".*?\"', data)
s=re.findall(r'href=\"https://.*?\"',data)
links=[]
i=0;
while(i<len(s)):
    string=s[i]
    links.append(string[6:-1])
    i=i+1


#newdata= re.search(regex, data)
#print(newdata)
