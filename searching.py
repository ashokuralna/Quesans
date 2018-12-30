import urllib.request
import re
baseurl="https://www.bing.com/search?q="
oquery="who is the prime minister of India?"
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
print(len(links))
webdata=[]

for i in range(len(links)):
    webdata.append((urllib.request.urlopen(links[i]).read()))

k = []
j = 0;
while (j < len(webdata)):
    k.append(str(webdata[j]))
    j = j + 1
    #print(k)

l = 0;
t = []
while (l < len(k)):
    t.append(re.findall(r"<p>.*</p>", k[l]))
    l = l + 1
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])



