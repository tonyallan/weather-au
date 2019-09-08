#

import bs4 # uses lxml
import urllib.request


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

uv_PRODUCT_URL = {
    'ACT': 'ftp://ftp.bom.gov.au/anon/gen/fwo/IDZ00107.xml',
    'NSW': 'ftp://ftp.bom.gov.au/anon/gen/fwo/IDZ00107.xml',
    'NT':  'ftp://ftp.bom.gov.au/anon/gen/fwo/IDZ00108.xml',
    'Qld': 'ftp://ftp.bom.gov.au/anon/gen/fwo/IDZ00109.xml',
    'SA':  'ftp://ftp.bom.gov.au/anon/gen/fwo/IDZ00110.xml',
    'Tas': 'ftp://ftp.bom.gov.au/anon/gen/fwo/IDZ00111.xml',
    'Vic': 'ftp://ftp.bom.gov.au/anon/gen/fwo/IDZ00112.xml',
    'WA':  'ftp://ftp.bom.gov.au/anon/gen/fwo/IDZ00113.xml'
    }

PLACES_URL = 'http://www.bom.gov.au/places/{state}/{location}'

PLACES_USER_AGENT = \
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 ' \
    '(KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

# UV Index Forecast - Local Noon
UV_INDEX_URL = 'http://reg.bom.gov.au/fwo/IDY00508.gif'


# Helper functions
# https://stackoverflow.com/questions/49639450/scraping-xml-data-with-bs4-lxml

def fetch_xml(url):
    
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()

    return bs4.BeautifulSoup(r, 'xml')
