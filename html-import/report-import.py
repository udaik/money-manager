import sys
import unicodedata
from bs4 import BeautifulSoup
import transaction


def normalize_str(str):
    return unicodedata.normalize('NFKD', unicode(str)).encode('ascii', 'ignore')


def import_html_file(filename):
    html_str = open(filename, 'r').read()
    soup = BeautifulSoup(open(filename, 'r').read(), 'html.parser')
    print "soup children", len(soup.contents)
    print "body children", len(soup.body.contents)
    i = 0
    for child in soup.body.children:
        print "-------------------------------------------------------------"
        print "str", normalize_str(soup.body.child).rstrip(), "33"
        if len(normalize_str(child).rstrip()) == 0:
            continue
        else:
            print i, child
            i += 1
        pass  # print "XXXXXXXXX", (child)
    # print len(soup.tbody.contents[0]), soup.tbody.contents

    """ trxs = []
    for tr in soup.find_all('tbody'):
        for td in tr.find_all('td'):
            print "YYYY"
            for span in td.find_all('span'):
                print "XXX"
                for index, item in enumerate(span.children, start=0):
                    s = normalize_str(item)
                    print s.rstrip(), type(s)"""


if __name__ == "__main__":
    import_html_file(sys.argv[1])
