with open('./words/nouns.txt') as f:
    nouns = list(map(lambda w: w.strip(), f.readlines()))