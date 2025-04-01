import sys
import requests
import bs4

if __name__ == '__main__':
    url, tag, attribute, output = sys.argv[1:]

    while attribute != "final":
        html = requests.get(url).text
        soup = bs4.BeautifulSoup(html, features="html.parser")
        found_tags = soup.find_all(tag)
        for tag in found_tags:
            temp = tag.get(attribute)
            if temp:
                found_attr = temp
        url, tag, attribute = found_attr.split(",")

    html = requests.get(url).text
    soup = bs4.BeautifulSoup(html, features="html.parser")
    found_tags = soup.find_all(tag)
    for tag in found_tags:
        temp = tag.get(attribute)
        if temp:
            found_attr = temp
    with open(output, 'w') as f:
        f.write(found_attr)