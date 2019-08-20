from webscrape1 import simple_get, log_error
from bs4 import BeautifulSoup

# url = 'http://www.fabpedigree.com/james/mathmen.htm'
# raw_html = simple_get(url)
# html = BeautifulSoup(raw_html, 'html.parser')
# for i, li  in enumerate(html.select('li')):
#     print(i, li.text)


"""
The get_names() function downloads the page and iterates over the <li> elements, 
picking out each name that occurs. Next, you add each name to a Python set, 
which ensures that you don’t end up with duplicate names. 
Finally, you convert the set to a list and return it.
"""
def get_names():
    """
    Downloads the page where the list of mathematicians is found
    and returns a list of strings, one per mathematician
    """
    url = 'http://www.fabpedigree.com/james/mathmen.htm'
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        names = set()
        for li in html.select('li'):
            for name in li.text.split('\n'):
                if len(name) > 0:
                    names.add(name.strip())
        return list(names)

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))


def get_hits_on_name(name):
    """
    Accepts a `name` of a mathematician and returns the number
    of hits that mathematician's Wikipedia page received in the
    last 60 days, as an `int`
    """
    # url_root is a template string that is used to build a URL.
    url_root = 'URL_REMOVED_SEE_NOTICE_AT_START_OF_ARTICLE'
    response = simple_get(url_root.format(name))

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')

        hit_link = [a for a in html.select('a')
                    if a['href'].find('latest-60') > -1]

        if len(hit_link) > 0:
            # Strip commas
            link_text = hit_link[0].text.replace(',', '')
            try:
                # Convert to integer
                return int(link_text)
            except:
                log_error("couldn't parse {} as an `int`".format(link_text))

    log_error('No pageviews found for {}'.format(name))
    return None

result = get_names()
print(result)
print(get_hits_on_name('Blaise Pascal'))