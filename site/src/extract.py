import re
from block import *

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if re.match(r'^#{1} ', line):
            heading_text = line.lstrip('#').strip()
            return heading_text    
    else:
        raise Exception (f'incorrect heading')
    
