from bs4 import BeautifulSoup
import requests
import time
from multiprocessing.pool import ThreadPool
import os
import zipfile
import concurrent.futures

## Support Functions
def list_files_on_address(url, ext=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
def p_donwload_single_file(args):
    url = args[0]
    save_path = args[1]
    print(f'downloading {url} to {save_path} ')
   
    t0 = time.time()
    try:
        r = requests.get(url)
        with open(save_path, 'wb') as f:
            f.write(r.content)
        print(f'{save_path} downloaded in {round(time.time()-t0,2)} seconds')
    except Exception as e:
        print(f'error downloading {url}', e)
def p_delete_single_file(args):
    path=args[0]
    t0 = time.time()
    os.remove(path)
    return(path,time.time()-t0)
def p_unzip_single_file(args):
    file = args[0]
    path = args[1]
    t0 = time.time()
    f = zipfile.ZipFile(file)
    f.extractall(path)
    return(path, time.time()-t0)

def m_call(fn, args, workers = 5, mode="p", verbose = True):
    t0 = time.time()
    ret = []
    
    if mode == "p":
        with concurrent.futures.ProcessPoolExecutor(max_workers = workers) as executor:
            futures = []
            for item in args:
                futures.append(executor.submit(fn,item))
            for future in concurrent.futures.as_completed(futures):
                ret.append(future.result())
    
    if mode == "t":
        with concurrent.futures.ThreadPoolExecutor(max_workers = workers) as executor:
            futures = []
            for item in args:
                futures.append(executor.submit(fn,item))
            for future in concurrent.futures.as_completed(futures):
                ret.append(future.result())
                
    if mode == "s":
        for arg in args:
            ret.append(fn(arg))

    if verbose:
        print(f'mode: {mode}, size:{len(args)}, duration: {round(time.time()-t0,2)}, workers: {workers}')

    return ret

