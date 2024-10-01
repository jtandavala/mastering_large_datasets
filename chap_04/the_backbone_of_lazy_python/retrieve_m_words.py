words = ["apple","mongoose","walk","mouse","good", "pineapple","yeti","minnesota","mars", "phone","cream","cucumber","coffee","elementary", "sinister","science","empire"]

def contains_m(word):
    if 'm' in word.lower(): return True
    else: return False

m_words = filter(contains_m, words)

next(m_words)

print(list(m_words))
