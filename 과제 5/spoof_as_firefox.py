import requests


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:64.0) Gecko/20100101 Firefox/64.0'}
URL = 'http://www.google.com'


def spoof_firefox():
    response = requests.get(URL, headers=headers)
    print(response.headers)


if __name__ == '__main__':
    spoof_firefox()