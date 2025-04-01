from urllib.parse import urlparse, urljoin

import bs4
import requests


def get_domain(url):
    parsed = urlparse(url)
    valid_schemes = ["https", "http"]
    if parsed.scheme in valid_schemes and parsed.netloc:
        return f"{parsed.scheme}://{parsed.netloc}"
    return ""


def combine_paths(url, path):
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}{path}"


def combine_urls(url1, url2):
    return urljoin(url1, url2)


def print_pages(url, paths, output):
    with open(output, "w") as f:
        base = url
        for path in paths:
            combined = combine_urls(base, path)
            req = requests.get(combined)
            soup = bs4.BeautifulSoup(req.text, features="html.parser")
            f.write(f"{soup.get_text()}\n")
            base = combined