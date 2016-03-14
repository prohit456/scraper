import urllib2;
from BeautifulSoup import BeautifulSoup as bs;

page = urllib2.urlopen("https://en.wikipedia.org/wiki/Mahabalipuram").read();
soup = bs(page);
soup.prettify();
#print soup;

urls = [];
link_dict = {};
for anchor in soup.findAll('a', href=True, title=True):
    #print anchor;
    print "anchor:", anchor['href'];
    #if (anchor['href'][0:3] == '/en'):
    urls.append (anchor['href']);
print "url", urls;
titles = [];
name = raw_input("title");
for anchor in soup.findAll('title'):
    print anchor;
    name = raw_input("title");

for url in urls:
    page = urllib2.urlopen("http://en.wikipedia.org"+url).read();
    soup = bs(page);
    soup.prettify();
    srls = [];
    for anchor in soup.findAll('p', 'a', href=True):
        print anchor['href'];
	if anchor['href'] not in urls:
	    urls.append(anchor['href']);
    #name = raw_input("Press enter");
    print url[4:], url;
    if url[4:] not in link_dict.keys():
        link_dict[url[4:]] = "http://en.wikipedia.org" + url;
    #name = raw_input("Press enter");
print "Done with scraping";
#print link_dict;  
#f = open ('dct', 'w');
#f.write(repr(link_dict));
#for key in link_dict.keys():
#    url = link_dict[key];
#    page = urllib2.urlopen(url).read();
#    soup = bs (page);
#    soup.prettify();
#    for anchor in soup.findAll('p'):
#        print anchor;
#	#name = raw_input("press enter");
