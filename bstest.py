from bs4 import BeautifulSoup
import urllib2
import io

url = "https://en.wikipedia.org/wiki/Bro_(subculture)"


# soup.find_all('bro')

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content, "lxml")
# soup = BeautifulSoup(html_doc, 'html.parser')

# print soup.prettify()

# prints all links
# for link in soup.find_all('a'):
#     print(link.get('href'))

newline = '\n'
# Unicode
print soup.title.string
bros = soup.get_text('bro').replace(' ', '\n') 

# String
# bros = soup.find(text="bro")

# print bros


# Unicode
with io.open('brodum.txt', 'w') as f:
    f.write(bros)

# f = open("bros.txt")
# print(f.readlines())

text_file = open("bros.txt", "r")
lines = text_file.readlines()
print lines
print len(lines)
text_file.close()

# for line in open("bros.txt"):
#     line = line.strip()
    # name, vote = line.split(" - ", )
    # munge the vote string to clean it up
    # vote = vote.strip().capitalize()
    # if not vote in counts:
    #     # First vote for this variety
    #     counts[vote] = 1
    # else:
    #     # Increment the vote count
    #     counts[vote] = counts[vote] + 1
# print (line)


# STRING
# with open("brodum.txt", "w") as text_file:
#     text_file.write("Purchase Amount: {0}".format(bros))

# f = open('brodum.txt','r')
# f.write(soup.get_text('bro').replace(' ', '\n') )
# print soup.find_all(text=True)
# print soup.find(text="bro")
# print soup.find_all(string=True)



