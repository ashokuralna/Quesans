try:
    from googlesearch import search
except ImportError:
        print("No module name google found")

# to search
query= "python"

for j in search(query, tld='co.in', num=10, start=0, stop=None, pause=2):
    print(j)