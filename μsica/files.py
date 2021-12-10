# -*- coding: utf8


import requests
import shutil
import sys
import tqdm
import warnings


def download(url, outfpath, verify=True):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        filesize = int(requests.head(url).headers["Content-Length"])
        bar = tqdm.tqdm(unit="B",
                        unit_scale=True,
                        unit_divisor=1024,
                        total=filesize,
                        file=sys.stdout,
                        desc=outfpath)

        with requests.get(url, stream=True, verify=verify) as r:
            # r.raise_for_status()
            with open(outfpath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    f.write(chunk)
                    datasize = f.write(chunk)
                    bar.update(datasize)

                
            
def extract(zipfpath, where):
    shutil.unpack_archive(zipfpath, where)
