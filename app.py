# Author: Orion Ford
# This program allows you to donwload images from Instagram.

import requests
from bs4 import BeautifulSoup

start_url = input('Input your link: ')
response = requests.get(start_url)
html = response.text

soup = BeautifulSoup(html, 'lxml')
photo_url = soup.find('meta', property="og.image")['content']
print(photo_url)

# extract some character of photo)url in order to name the photo

photo_name = photo_url[-25:-6]
print('Photo name is:' + photo_name)


requests_url = requests.get(photo_url)
f = open(photo_name + '.jpg', 'ab')
f.write(requests_url.content)
print('Processing')
f.close()
print('Download Complete')


def request_start_url(start_url):
    soup = BeautifulSoup(requests_url, 'lxml')
    photo_url = soup.find('meta', property='og:image')
    print(photo_url)
    print(photo_url['content'])
    return photo_url['content']


def downloader(photo_url):

    # Extract some character of photo_url in order to name the photo

    photo_name = photo_url[-25:6]
    print('Photo nmae is:' + photo_name)
    requests_url = requests.get(photo_url)
    f = open(photo_name + '.jpg', 'ab')
    f.write(requests_url.content)
    print('Processing')
    f.close()
    print('Download complete')


def main():
    start_url = input('Input your link:')
    requests_url = requests_start_url(start_url)
    photo_url = find_photo_url(requests_url)
    downloader(photo_url)


if __name__ == '__main__':
    main()
