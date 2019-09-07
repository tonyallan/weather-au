#

import bs4 # uses lxml
import urllib.request
#import xml.dom.minidom


# Weather Data Services
# http://www.bom.gov.au/catalogue/data-feeds.shtml

ANON_GEN_FTP = 'ftp://ftp.bom.gov.au/anon/gen/'

PRODUCT_PREFIX = {
    'ACT': 'IDN',   # Australian Capital Territory
    'NSW': 'IDN',   # New South Wales
    'NT':  'IDD',   # Northern Territory
    'Qld': 'IDQ',   # Queensland
    'SA':  'IDS',   # South Australia
    'Tas': 'IDT',   # Tasmania
    'Vic': 'IDV',   # Victoria
    'WA':  'IDW'    # Western Australia
    }

OBSERVATION_PRODUCT_URL = {
    'ACT': 'ftp://ftp.bom.gov.au/anon/gen/fwo/IDN60920.xml',
    'NSW': 'ftp://ftp.bom.gov.au/anon/gen/fwo/IDN60920.xml',
    'NT':  'ftp://ftp.bom.gov.au/anon/gen/fwo/IDD60920.xml',
    'Qld': 'ftp://ftp.bom.gov.au/anon/gen/fwo/IDQ60920.xml',
    'SA':  'ftp://ftp.bom.gov.au/anon/gen/fwo/IDS60920.xml',
    'Tas': 'ftp://ftp.bom.gov.au/anon/gen/fwo/IDT60920.xml',
    'Vic': 'ftp://ftp.bom.gov.au/anon/gen/fwo/IDV60920.xml',
    'WA':  'ftp://ftp.bom.gov.au/anon/gen/fwo/IDW60920.xml'
    }


# Helper functions

def fetch_xml(url):
    
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()

    return bs4.BeautifulSoup(r.decode('utf-8'), 'lxml')

