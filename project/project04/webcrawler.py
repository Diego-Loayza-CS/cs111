import sys
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from RequestGuard import RequestGuard
from urllib.parse import urlparse, urljoin
from image_processing import sepia, grayscale, flipped, mirror


def get_full_url(url, href):
    if href is None:
        return None
    href = href.split("#")[0]

    if href and urlparse(href).scheme in ["http", "https"]:
        if "#" in href:
            href = href.split("#")[0]
        full_url = href

    elif href and href[0] == "/":
        full_url = f"{urlparse(url).scheme}://{urlparse(url).netloc}{href}"

    else:
        full_url = urljoin(url, href)

    return full_url


def process_hist_list(string):
    string = string[1:-1]
    return string.split()


def count_links(args):
    url, output1, output2 = args[1], args[2], args[3]
    guard = RequestGuard(url)

    visit_links = [url]
    counts = {}

    i = 0
    while i < len(visit_links):
        if visit_links[i] in counts:
            counts[visit_links[i]] += 1
        else:
            counts[visit_links[i]] = 1

            page = guard.make_get_request(visit_links[i])
            if page:
                html = BeautifulSoup(page.text, "html.parser")

                for tag in html.find_all("a"):
                    href = tag.get("href")
                    if href:
                        full_url = get_full_url(visit_links[i], href)
                        if full_url and guard.can_follow_link(full_url):
                            visit_links.append(full_url)
                        else:
                            if full_url in counts:
                                counts[full_url] += 1
                            else:
                                counts[full_url] = 1

        i += 1

    values = []
    for value in counts:
        values.append(counts[value])

    bins = []
    for i in range(max(values) + 1):
        bins.append(i + 1)

    plt.clf()
    hist_values, hist_bins, non_used = plt.hist(values, bins)
    plt.savefig(output1)

    hist_val_list = process_hist_list(str(hist_values))
    hist_bin_list = process_hist_list(str(hist_bins))

    with open(output2, "w") as f:
        for i in range(len(hist_val_list)):
            i_val = float(hist_val_list[i])
            i_bin = float(hist_bin_list[i])
            f.write(f"{i_bin:.1f},{i_val:.1f}\n")


def get_values(values, index):
    new_values = []
    for value in values:
        new_values.append(value[index])
    return new_values


def plot_data(args):
    url, output1, output2 = args[1], args[2], args[3]
    req = requests.get(url)

    if not req:
        print("not an url")
        return

    soup = BeautifulSoup(req.text, "html.parser")
    table = soup.find("table", id="CS111-Project4b")

    x_values = []
    y_values = []

    rows = table.find_all("tr")
    for row in rows:
        columns = row.find_all("td")
        values = []
        for column in columns:
            values.append(column.text)
        x_values.append(float(values[0]))
        y_values.append([float(i) for i in values[1:]])

    colors = ["b", "g", "r", "k"]
    plt.clf()

    for i in range(len(y_values[0])):
        y_column = get_values(y_values, i)
        plt.plot(x_values, y_column, colors[i])

    plt.savefig(output1)

    with open(output2, "w") as f:
        for i in range(len(x_values)):
            x = float(x_values[i])
            f.write(f"{x}")
            for j in range(len(y_values[i])):
                y = float(y_values[i][j])
                f.write(f",{y}")
            f.write("\n")


def image_manipulation(args):
    url, output_prefix, selected_filter = args[1], args[2], args[3]
    guard = RequestGuard(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    image_list = []
    files = []
    tags = soup.find_all("img")
    for tag in tags:
        img_name = tag.get("src")
        full_url = get_full_url(url, img_name)
        image_list.append(full_url)
        response = guard.make_get_request(full_url, use_stream=True)
        with open(img_name, 'wb') as f:
            f.write(response.content)
        files.append(img_name)


    for file in files:
        output = f"{output_prefix}{file}"
        adjusted_args = [selected_filter, file, output]
        if adjusted_args[0] == "-s":
            sepia(adjusted_args)
        elif adjusted_args[0] == "-g":
            grayscale(adjusted_args)
        elif adjusted_args[0] == "-f":
            flipped(adjusted_args)
        elif adjusted_args[0] == "-m":
            mirror(adjusted_args)
        else:
            print("Invalid Command")




def check_args(args, i):
    if len(args) == i:
        return True
    print("invalid arguments")
    raise SystemExit


def valid_filter(args):
    if args[3] == "-s" or args[3] == "-g" or args[3] == "-f" or args[3] == "-m":
        return True
    print("invalid arguments")
    raise SystemExit


def validate_commands(args):
    if args[0] == "-c":
        if check_args(args, 4):
            count_links(args)
    elif args[0] == "-p":
        if check_args(args, 4):
            plot_data(args)
    elif args[0] == "-i":
        if check_args(args, 4) and valid_filter(args):
            image_manipulation(args)
    else:
        print("invalid arguments")
        raise SystemExit


def main(args):
    if args and len(args) > 1:
        validate_commands(args[1:])
    else:
        print("invalid arguments")
        raise SystemExit


if __name__ == '__main__':
    main(sys.argv)