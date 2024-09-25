import re
from toolz.functoolz import compose
from util.func import replace_7t, replace_3e, replace_6g, replace_4a


class ChineseMatcher:
    def __init__(self):
        self.r = re.compile(r"[\u4e00-\u9fff]+")

    def sub_chinese(self, s):
        return self.r.sub(" ", s)


sample_messages = [
    "7his所is家4没s4mpl3动m3ss463",
    "don7家73ll经4nyon3法7his现m3ss463",
    "w3现4r3当b3in6进so好s3cr3t",
    "733小h33成h33去nobody看is天on分7o理us",
    "w3么will面n3v3r分637理c4u6ht",
    "w3事4r3经such没sn34ky天h4ckers",
]

matcher = ChineseMatcher()


hacker_translate = compose(
    matcher.sub_chinese, replace_4a, replace_6g, replace_3e, replace_7t
)

result = map(hacker_translate, sample_messages)
print(list(result))
