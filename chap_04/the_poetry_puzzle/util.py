import toolz
import itertools
from glob import iglob

def word_is_desired(w):
    return w in ["a","the"]

def word_ratio(d):
    return float(d.get("a", 0)) / float(d.get("the", 0.0001))

def analyze_poems(poems, cleaner):
    return word_ratio(
        toolz.frequencies(
            filter(word_is_desired,
                itertools.chain(*map(cleaner.clean_poem, poems)))))
