from leafnode import *
from split import *


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url)
    def __repr__(self):
        urlstr = f"'{self.url}'" if self.url is not None else "None"
        return f'TextNode({self.text}, {self.text_type}, {urlstr})'

def text_node_to_html_node(text_node):
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"
    if text_node.text_type == text_type_text:
        return leafnode(text_node.text)
    if text_node.text_type == text_type_bold:
        return leafnode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return leafnode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return leafnode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return leafnode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return leafnode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception(f'text_type is incorrect')
