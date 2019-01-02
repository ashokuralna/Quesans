import urllib.request
from inscriptis import get_text
from nltk.corpus import stopwords
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
   # print("This is tokenized data number ",k)
    #print(tokenized_data[k])
    k=k+1

stop_words = set(stopwords.words('english'))
#print(tokenized_data)
filtered_sentence = []

i=0
while(i<len(tokenized_data)):
    newword_list=[]
    for w in tokenized_data[i]:
        if w not in stop_words:
            newword_list.append(w)
    filtered_sentence.append(newword_list)
    i=i+1
#print(filtered_sentence)

#for items in filtered_sentence:
 #   print(items)
nouns_list=[]
for r in range(len(filtered_sentence)):
    word_list = []
    for word,pos in nltk.pos_tag(filtered_sentence[r]):
         # print(pos)
         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
             word_list.append(word)
    nouns_list.append(word_list)

print(nouns_list)

for items in nouns_list:
    print(items)



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
