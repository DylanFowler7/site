

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props =props
    def to_html(self):
        if self.tag is None:
            return self.value or ""
        attrs = ""
        if self.props:
            for key, value in self.props.items():
                attrs += f' {key}="{value}"'
        if self.value is not None and not self.children:
            return (f'<{self.tag}{attrs}>{self.value}</{self.tag}>')
        children_html = ""
        if self.children:
            for child in self.children:
                children_html += child.to_html()
        inner_html = (self.value or "") + children_html
        return (f'<{self.tag}{attrs}>{inner_html}</{self.tag}>')
    def props_to_html(self):
        string = []
        if self.props == None:
            return ""
        if self.props == "":
            return ""
        for prop, value in self.props.items():
            string.append(f'{prop}="{value}"')   
        return (" ".join(string))
    def __repr__(self):
        return (f'HTMLNode is {self.tag}, {self.value}, {self.children}, {self.props}')

