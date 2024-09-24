"""
Why using pathos: We use pathos because the builtin multiprocessing
can pickle all object, namely

- Lambda functions
- Nested functions
- Nested classes
"""

import time
from urllib import request
from typing import List
from pathos.multiprocessing import ProcessPool

links = [
    "/2024/8/17/django-para-iniciantes/",
    "/2024/8/17/system-design-for-senior-developer/",
    "/2024/8/17/backend-engineering/",
    "/2024/8/17/machine-learning-for-web-developers/"
]

def blog_downloader(links: List[str]):
    for link in links:
        yield f"http://127.0.0.1:8000/blog{link}"

def get_url(path: str):
    return request.urlopen(path).read()

if __name__ == '__main__':
    with ProcessPool() as P:
        start = time.time()
        blog_posts = P.map(get_url, blog_downloader(links))
        print(len(blog_posts))
        end = time.time()
        print(f'{end-start:.4f}')
