import urllib2
from random import randint
def getRandom(num):
    response = urllib2.urlopen('http://en.wikipedia.org/wiki/Special:Random')
    html = response.read()
    html = html.replace(" ", "")
    htmllen = len(html)
    #I especially love how I still grab a random number here
    l =  randint(0, htmllen - num)
    data = html[l:l+num]
    return [ ord(x) for x in list(data) ]

print getRandom(25)
