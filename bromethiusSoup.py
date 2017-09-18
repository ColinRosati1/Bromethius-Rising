from bs4 import BeautifulSoup
import urllib2
import io

url = "https://en.wikipedia.org/wiki/Bro_(subculture)"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content, "lxml")

# Unicode
print soup.title.string
bros = soup.get_text('bro').replace(' ', '\n') 


# Unicode
with io.open('brodum.txt', 'w') as f:
    f.write(bros)

text_file = open("bros.txt", "r")
lines = text_file.readlines()
print lines
print len(lines)
text_file.close()




