import urllib

def read_URL(url):
    fhand = urllib.urlopen(url).read()
    print fhand

read_URL("http://www.fulltilt.com/about-us/system-faq")
