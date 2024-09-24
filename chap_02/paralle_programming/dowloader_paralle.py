"""
Problems we can encounter in Parallelization code: Using Python builting
multiprocessing tool

1. The inability to pickle data or functions, causing our programs to not run
2. Order-sensitive operations returning inconsistent results
3. State-dependent operations returning inconsistent results
"""

from urllib import request
import time
from typing import List
from multiprocessing import Pool

links = [
    "/2024/8/17/django-para-iniciantes/",
    "/2024/8/17/system-design-for-senior-developer/",
    "/2024/8/17/backend-engineering/",
    "/2024/8/17/machine-learning-for-web-developers/"
]

def blog_downloader(links: List[str]):
    for link in links:
        yield f"http://127.0.0.1:8000/blog{link}"

def get_url(path):
    return request.urlopen(path).read()

if __name__ == '__main__':

    with Pool() as P:
         start = time.time()
         blog_posts = P.map(get_url, blog_downloader(links))
         print(len(blog_posts))
         end = time.time()
         print(f'{end-start:.4f}')
