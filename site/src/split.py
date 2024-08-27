from textnode import *
from extract import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for nodes in old_nodes:
        if nodes.text_type == text_type_text:
            split_nodes = nodes.text.split(delimiter)
            if len(split_nodes) % 2 == 0:
                raise Exception (f'invalid Markdown syntax')
            for index, value in enumerate(split_nodes):
                if index % 2 == 0:
                    new_node = TextNode(value, text_type_text)
                    node_list.append(new_node)
                else:
                    new_node = TextNode(value, text_type)
                    node_list.append(new_node)
        else:
            node_list.append(nodes)
    return node_list

def split_nodes_image(old_nodes):
    image_list = []
    non_image_list = []
    for images in old_nodes:
        if images.text_type == text_type_image:
            images_ext = extract_markdown_images(images.text)
            for value in images_ext:
                new_image = TextNode(value[0], text_type_image, value[1])
                image_list.append(new_image)
        if images.text_type != text_type_image:
            if images.text == "":
                continue
            non_image_list.append(TextNode(images.text, images.text_type))
    return image_list + non_image_list

def split_nodes_link(old_nodes):
    link_list = []
    non_link_list = []
    for links in old_nodes:
        if links.text_type == text_type_link:
            links_ext = extract_markdown_links(links.text)
            for value in links_ext:
                new_link = TextNode(value[0], text_type_link, value[1])
                link_list.append(new_link)
        if links.text_type != text_type_link:
            if links.text == "":
                continue
            non_link_list.append(TextNode(links.text, links.text_type))
    return link_list + non_link_list

def text_to_textnodes(text):
    nodes = []
    image_splits = extract_markdown_images(text)
    current_index = 0
    for image_text, image_url in image_splits:
        start_index = text.find(f"![{image_text}]({image_url})", current_index)
        if start_index > current_index:
            nodes.append(TextNode(text[current_index:start_index], text_type_text))
        nodes.append(TextNode(f"![{image_text}]({image_url})", text_type_image))
        current_index = start_index + len(f"![{image_text}]({image_url})")
    if current_index < len(text):
        nodes.append(TextNode(text[current_index:], text_type_text))
    new_nodes = []
    for node in nodes:
        if node.text_type == text_type_text:
            link_splits = extract_markdown_links(node.text)
            current_index = 0
            for link_text, link_url in link_splits:
                start_index = node.text.find(f"[{link_text}]({link_url})", current_index)
                if start_index > current_index:
                    new_nodes.append(TextNode(node.text[current_index:start_index], text_type_text))
                new_nodes.append(TextNode(f"[{link_text}]({link_url})", text_type_link))
                current_index = start_index + len(f"[{link_text}]({link_url})")
            if current_index < len(node.text):
                new_nodes.append(TextNode(node.text[current_index:], text_type_text))
            

    def apply_delimiter_splits(nodes, delimiter, text_type):
        new_nodes = []
        for node in nodes:
            if node.text_type == text_type_text:
                new_nodes.extend(split_nodes_delimiter([node], delimiter, text_type))
        return new_nodes
    new_nodes = nodes
    new_nodes = apply_delimiter_splits(new_nodes, "**", text_type_bold)
    print("After bold split:", new_nodes)
    new_nodes = apply_delimiter_splits(new_nodes, "*", text_type_italic)
    print("After italic split:", new_nodes)
    new_nodes = apply_delimiter_splits(new_nodes, "`", text_type_code)
    print("After code split:", new_nodes)
    return new_nodes
