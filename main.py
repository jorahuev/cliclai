import concurrent.futures
from xbrowser import XBrowser

# Create a list of URLs
urls = [
    'https://www.google.com/',
    'https://www.wikipedia.org/',
    'https://www.youtube.com/',
    'https://www.github.com/',
    'https://www.python.org/'
]

# Set the maximum number of threads to 2
max_threads = 2

# Create an instance of the XBrowser class for each URL and navigate to the URL
with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
    for url in urls:
        browser = XBrowser()
        executor.submit(browser.get, url)
