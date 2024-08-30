import os
from textnode import *
import shutil
from block import *
from htmlnode import *
from split import *

def main():
    source_dir_path = './static'
    dest_dir_path = os.path.expanduser('~/site/public')
    create_static(source_dir_path, dest_dir_path)
    dir_path_content = os.path.expanduser('~/site/src/content')
    template_path = os.path.expanduser('~/site/src/template.html')
    dest_dir_path = os.path.expanduser('~/site/public')
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)

def create_static(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for filename in os.listdir(source_dir_path):
        old_path = os.path.join(source_dir_path, filename)
        new_path = os.path.join(dest_dir_path, filename)
        print(f' * {old_path} -> {new_path}')
        if os.path.isfile(old_path):
            shutil.copy(old_path, new_path)
        else:
            create_static(old_path, new_path)
        

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path, 'r') as file:
        from_content = file.read()
    with open(template_path, 'r') as file:
        template_content = file.read()
    html_node = markdown_to_html_node(from_content)
    from_markdown = html_node.to_html()
    from_title = extract_title(from_content)
    replaced = template_content.replace("{{ Title }}", from_title).replace("{{ Content }}", from_markdown)
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
       os.makedirs(dest_dir)
    with open(dest_path, 'w') as file:
        file.write(replaced)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(full_path) and entry.endswith('.md'):
            with open(full_path, 'r') as file:
                from_content = file.read()
            with open(template_path, 'r') as file:
                template_content = file.read()
            html_node = markdown_to_html_node(from_content)
            from_markdown = html_node.to_html()
            from_title = extract_title(from_content)
            replaced = template_content.replace("{{ Title }}", from_title).replace("{{ Content }}", from_markdown)
            new_dest_path = os.path.join(dest_dir_path, entry.replace('.md', '.html'))
            dest_dir = os.path.dirname(new_dest_path)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            with open(new_dest_path, 'w') as file:
                file.write(replaced)
        elif os.path.isdir(full_path):
            generate_pages_recursive(full_path, template_path, os.path.join(dest_dir_path, entry))


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")



if __name__ == "__main__":
    main()
