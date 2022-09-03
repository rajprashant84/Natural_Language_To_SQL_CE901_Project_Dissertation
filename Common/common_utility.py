def line_Count(filename):
    with open(filename) as fname:
        return sum(1 for line in fname)

def remove_token(tokens):
    ret =''
    for g, a in zip(tokens['gloss'], tokens['after']):
        ret += g + a
    return ret.strip()
