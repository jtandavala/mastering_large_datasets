"""
Run un:
    1000
    939.2931
"""
import json
import time
from urllib import request, parse

def link_to_title(link):
    return link["title"]

def clean_if_key(page, key):
    if key in page.keys():
        return map(link_to_title, page[key])
    else: return []

def build_url(safe_title):
    return (
            f"https://en.wikipedia.org/w/api.php?"
            f"action=query&prop=links|linkshere&pllimit=500&lhlimit=500"
            f"&titles={safe_title}&format=json&formatversion=2"
        )

def get_wiki_links(page_title):
    safe_title = parse.quote(page_title)
    url = build_url(safe_title)
    page = request.urlopen(url).read()
    j = json.loads(page)
    jpage = j["query"]["pages"][0]
    inbound = clean_if_key(jpage, "links")
    outbound = clean_if_key(jpage, "linkshere")
    return {
        "title": page_title,
        "in_links": list(inbound),
        "out_links": list(outbound)
    }

def flatten_network(page):
    return page["in_links"] + page["out_links"]

if __name__ =='__main__':
    start = time.time()
    root = get_wiki_links("Parallel_computing")
    initial_network = flatten_network(root)
    all_pages = []
    start = time.time()
    for link in initial_network:
        item = get_wiki_links(link)
        all_pages.append(item)
    print(len(all_pages))
    end = time.time()
    print(f'{end-start:.4f}')


    # print(initial_network)
    # print(len(initial_network))
    # print()
    # end = time.time()
    # print(f'{end-start:.4f}')
