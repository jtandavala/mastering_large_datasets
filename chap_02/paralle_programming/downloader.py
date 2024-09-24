import time
from urllib import request, error

links = [
    "/2024/8/17/django-para-iniciantes/",
    "/2024/8/17/system-design-for-senior-developer/",
    "/2024/8/17/backend-engineering/",
    "/2024/8/17/machine-learning-for-web-developers/"
]

def blog_downloader(links):
    for link in links:
        yield f"http://127.0.0.1:8000/blog{link}"

def get_url(path):
    return request.urlopen(path).read()


start = time.time()
blog_posts = map(get_url, blog_downloader(links))
print(len(list(blog_posts)))
end = time.time()

print(f'{end-start:.4f}')
