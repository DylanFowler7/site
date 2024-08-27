from textnode import *
from extract import *
from split import *
from htmlnode import *
import re

def markdown_to_blocks(markdown):
    list_of_blocks = markdown.split("\n\n")
    removed = []
    for block in list_of_blocks:
        stripped = block.strip()
        if stripped:
            removed.append(stripped)
    return removed

def block_to_block_type(block):
    if re.match(r'^#{1,6} ', block):
        return "heading"
    if block.startswith("```") and block.endswith ("```"):
        return "code"
    if all(line.startswith(">") for line in block.splitlines()):
        return "quote"
    if all(line.startswith(("* ", "- ")) for line in block.splitlines()):
        return "unordered_list"
    lines = block.splitlines()
    if all(line.startswith(f"{i}. ") for i, line in enumerate(lines, start=1)):
        return "ordered_list"
    return "paragraph"

def markdown_to_html_node(markdown):
    block = markdown_to_blocks(markdown)
    node_list = []
    parent_node = HTMLNode(tag="div", children=[])
    for each_block in block:
        block_type = block_to_block_type(each_block)
        if block_type == "heading":
            heading_level = len(each_block) - len(each_block.lstrip('#'))
            heading_text = each_block.lstrip('#').strip()
            htmlnode = HTMLNode(tag=f"h{heading_level}", value=heading_text)
            parent_node.children.append(htmlnode)
        if block_type == "code":
            pre_node = HTMLNode(tag="pre", children=[])
            code_node = HTMLNode(tag="code",value=each_block)
            pre_node.children.append(code_node)
            parent_node.children.append(pre_node)
        if block_type == "quote":
            htmlnode = HTMLNode(tag="blockquote", value=each_block)
            parent_node.children.append(htmlnode)
        if block_type == "unordered_list":
            ul_node = HTMLNode(tag="ul", children=[])
            items = each_block.strip().split('\n')
            for item in items:
                item_text = item.lstrip('- ').lstrip('* ').strip()
                li_node = HTMLNode(tag="li", value=item_text)
                ul_node.children.append(li_node)
            parent_node.children.append(ul_node)
        if block_type == "ordered_list":
            ol_node = HTMLNode(tag="ol", children=[])
            items = each_block.strip().split('\n')
            for item in items:
                item_text = re.sub(r'^\d+\.\s*', '', item).strip()
                li_node = HTMLNode(tag="li", value=item_text)
                ol_node.children.append(li_node)
            parent_node.children.append(ol_node)
        if block_type == "paragraph":
            htmlnode = HTMLNode(tag="p", value=each_block)
            parent_node.children.append(htmlnode)
    return parent_node
