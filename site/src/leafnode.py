from htmlnode import *
from textnode import *
from split import *

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, children=False, props=props)
    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        if not self.props:
            return (f'<{self.tag}>{self.value}</{self.tag}>')
        else:
            return (f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>')
            
