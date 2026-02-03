import requests
from urllib.parse import urlparse, urljoin
import re


class RequestGuard:
    def __init__(self, url):
        self.domain = urlparse(url).netloc
        self.forbidden = self.parse_robots()

    def can_follow_link(self, url):
        if re.search(self.domain, url):
            for item in self.forbidden:
                if re.search(rf"https://{self.domain}{item}.*", url):
                    return False
            return True
        return False

    def make_get_request(self, url, use_stream = None):
        if self.can_follow_link(url):
            return requests.get(url, stream = use_stream)


    def parse_robots(self):
        robots_url = f"https://{self.domain}/robots.txt"
        robots = requests.get(robots_url).text
        list_lines = robots.split(f"\n")[1:]

        forbidden_list = []
        for line in list_lines:
            item = re.search(r"Disallow: (.+)", line)
            if item:
                forbidden_list.append(item.group(1))

        return forbidden_list