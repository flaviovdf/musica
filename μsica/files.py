# -*- coding: utf8


import requests
import shutil
import sys
import tqdm
import warnings


def download(url, outfpath, verify=True):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        bar = tqdm.tqdm(unit="B",
                        unit_scale=True,
                        unit_divisor=1024,
                        file=sys.stdout,
                        desc=outfpath)

        with open(outfpath, 'wb') as f:
            with requests.get(url, stream=True, verify=verify) as r:
                for chunk in r.iter_content(chunk_size=4096): 
                    datasize = f.write(chunk)
                    bar.update(datasize)

                
            
def extract(zipfpath, where):
    shutil.unpack_archive(zipfpath, where)
