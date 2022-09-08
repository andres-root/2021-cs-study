

def find_substring(s):
    counter = 0
    l = 0
    h = 0
    length = 0
    
    hash_map = {}

    for c in s:
        if hash_map.get(c, False):
            hash_map[c] += 1
        else:
            hash_map[c] = 1

    while h < len(s):
        if hash_map[s[h]] > 0:
            counter += 1
        hash_map[s[h]] += 1
        h += 1