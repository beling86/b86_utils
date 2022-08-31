from bs4 import BeautifulSoup
import requests
import time

def browse(url, ext=''):
    """return the list of files under an http address

    Args:
        url (string): address to browse
        ext (str, optional): browse only specific extansion

    Returns:
        list of files
    """''
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

def p_dl(args):
    """Download a single file

    Args:
        args (list): args[0] -> URL to Download, args[1] -> Path to save
    """
    url = args[0]
    save_path = args[1]

    t0 = time.time()
    try:
        r = requests.get(url)
        with open(save_path, 'wb') as f:
            f.write(r.content)

    except Exception as e:
        print(f'error downloading {url}', e)