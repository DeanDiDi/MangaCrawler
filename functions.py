import requests
from bs4 import BeautifulSoup


def get_chapters(url: str) -> dict:
    """
    get all chapters' titles and urls
    :param url:
    :return: a dictionary of title : url paris
    """
    chapters = {}
    html = requests.get(url).text
    html = BeautifulSoup(html, 'html.parser')
    anchors = html.find('div', {'class': 'chapter-list'}).find_all('a')
    for a in anchors:
        chapters[a.get('title')] = a.get('href').rstrip()
    return chapters


def get_images(url: str) -> list:
    """
    :param url:
    :return: a list of url of images
    """
    html = requests.get(url).text
    lst = []
    html = BeautifulSoup(html, 'html.parser')
    images = html.find('div', {'id' : 'vungdoc'}).find_all('img')
    for image in images:
        lst.append(image.get('src'))
    return lst


def download_file(url: str, local_filename: str) -> None:
    """
    :param url: the url of image to be downloaded
    :param local_filename: the directory and name of the file
    :return: None
    """
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:   # filter out keep-alive new chunks
                f.write(chunk)
