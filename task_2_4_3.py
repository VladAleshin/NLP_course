import re
import sys

TOKENIZE_RE = re.compile(r'[а-яё]+|[+-]?\d*[,.]?\d+|\S{1}', re.I)
def tokenize(txt):
    return TOKENIZE_RE.findall(txt)
for line in sys.stdin:
    print(' '.join(tokenize(line.strip().lower())))


    
