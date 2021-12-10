# -*- coding: utf8


import requests
import shutil
import sys
import tqdm


def download(url, outfpath, verify=True):
    filesize = int(requests.head(url).headers["Content-Length"])
    bar = tqdm.tqdm(unit="B", # unit string to be displayed.
                    unit_scale=True, # let tqdm to determine the scale in kilo, mega..etc.
                    unit_divisor=1024, # is used when unit_scale is true
                    total=filesize, # the total iteration.
                    file=sys.stdout, # default goes to stderr, this is the display on console.
                    desc=outfpath) # prefix to be displayed on progress bar.
        
    with requests.get(url, stream=True, verify=verify) as r:
        r.raise_for_status()
        with open(outfpath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
                datasize = f.write(chunk)
                bar.update(datasize)
        
                
            
def extract(zipfpath, where):
    shutil.unpack_archive(zipfpath, where)
