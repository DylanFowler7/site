from htmlnode import *
from split import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props=props)
    def to_html(self):
        if not self.tag:
            raise ValueError (f'tag required')
        if not self.children:
            raise ValueError (f'children required')
        children_str = []
        for child in self.children:
            children_str.append(child.to_html())
        children_join = "".join(children_str)
        return (f'<{self.tag}{self.props_to_html()}>{children_join}</{self.tag}>')
