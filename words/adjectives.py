with open('./words/adjectives.txt') as f:
    adjectives = list(map(lambda w: w.strip(), f.readlines()))