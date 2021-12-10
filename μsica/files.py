# -*- coding: utf8


import requests
import shutil
import tqdm


def download(url, outfpath, verify=True):
    response = requests.get(url, stream=True, verify=verify)
    
    with open(outfpath, "wb") as handle:
        for data in tqdm.tqdm(response.iter_content()):
            handle.write(data)

            
def extract(zipfpath, where):
    shutil.unpack_archive(zipfpath, where)
