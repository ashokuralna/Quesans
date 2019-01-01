import urllib.request
from inscriptis import get_text
import re
from nltk.tokenize import word_tokenize
import nltk
baseurl="https://www.bing.com/search?q="
oquery="who is the chief minister of Delhi?"
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
print(links)
html=[]
text=[]
for j in range(len(links)):
    html.append(urllib.request.urlopen(links[j]).read().decode('utf-8'))
    text.append(get_text(html[j]))
    #print("This is text number ", j)
    #print(text[j])

tokenized_data=[]
k=0;
while(k<len(text)):
    tokenized_data.append(word_tokenize(text[k]))
    print("This is tokenized data number ",k)
    print(tokenized_data[k])
    k=k+1

 #empty to array to hold all nouns
count=0
word=[]
for r in range(len(tokenized_data)):
    for word,pos in nltk.pos_tag(nltk.word_tokenize(tokenized_data[r])):
        if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
            count+=1
            print(word)
            r=r+1






#print(len(links))
#print(links)
#webdata=[]

#for i in range(len(links)):
   # webdata.append((urllib.request.urlopen(links[i]).read()))

#k = []
#j = 0;
#while (j < len(webdata)):
  #  k.append(str(webdata[j]))
 #   j = j + 1
    #print(k)

#l = 0;
#t = []
#while (l < len(k)):
  #  t.append(re.findall(r"<p>.*</p>", k[l]))
  #  l = l + 1
