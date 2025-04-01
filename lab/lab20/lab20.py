import requests
import bs4


def download(url, output_filename):
    "*** YOUR CODE HERE ***"
    website = requests.get(url)
    with open(output_filename, "w") as file:
        file.write(website.text)


def make_pretty(url, output_filename):
    "*** YOUR CODE HERE ***"
    website = requests.get(url)
    bubble_website = bs4.BeautifulSoup(website.content, features="html.parser")
    with open(output_filename, "w") as file:
        file.write(bubble_website.prettify())


def find_paragraphs(url, output_filename):
    "*** YOUR CODE HERE ***"
    website = requests.get(url)
    bubble_website = bs4.BeautifulSoup(website.content, features="html.parser")
    paragraphs = bubble_website.find_all('p')
    with open(output_filename, "w") as file:
        for paragraph in paragraphs:
            file.write(f"{paragraph}\n")


def find_links(url, output_filename):
    "*** YOUR CODE HERE ***"
    website = requests.get(url)
    soup = bs4.BeautifulSoup(website.text, features="html.parser")
    tags = soup.find_all("a")
    with open(output_filename, "w") as file:
        for tag in tags:
            file.write(f"{tag.get('href')}\n")