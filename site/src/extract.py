import re
from block import *
from split import *

def extract_markdown_images(text):
    image = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return image
def extract_markdown_links(text):
    link = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return link
def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if re.match(r'^#{1} ', line):
            heading_text = line.lstrip('#').strip()
            return heading_text    
    else:
        raise Exception (f'incorrect heading')
    
