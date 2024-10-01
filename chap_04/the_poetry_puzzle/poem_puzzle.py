import toolz
import re, itertools
from glob import iglob
from util import word_ratio, word_is_desired, analyze_poems

class PoemCleaner:
    def __init__(self):
        self.r = re.compile(r'[.,;:!-]')
    def clean_poem(self, fp):
        with open(fp) as poem:
            no_punc = self.r.sub("",poem.read())
            return no_punc.lower().split()

if __name__ == '__main__':
    cleaner = PoemCleaner()
    author1_poems = iglob("A.txt")
    author2_poems = iglob("B.txt")

    author1_ratio = analyze_poems(author1_poems, cleaner)
    author2_ratio = analyze_poems(author2_poems, cleaner)

    print("""
         Original Poem: 0.3
         Author One: {:.2f}
         Authro Two: {:.2f}
        """.format(author1_ratio, author2_ratio))
