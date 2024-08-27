import os
from textnode import *
import shutil
from extract import *
from block import *
from htmlnode import *
from split import *

def main():
    static_dir = os.path.expanduser('~/site/static')
    public_dir = os.path.expanduser('~/site/public')
    create_static(static_dir, public_dir)
    from_path = os.path.expanduser('~/site/src/content/index.md')
    template_path = os.path.expanduser('~/site/src/template.html')
    dest_path = os.path.expanduser('~/site/public/index.html')
    generate_page(from_path, template_path, dest_path)

def create_static(static, public):
    if not os.path.exists(static):
        raise Exception(f'invalid path')
    try:
        if os.path.exists(public):
            shutil.rmtree(public)
        os.mkdir(public)
    except OSError as e:
        raise Exception(f'path creation error')
    for content in os.listdir(static):
        source_path = os.path.join(static, content)
        dest_path = os.path.join(public, content)
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
            print(f'copied {source_path} to {dest_path}')
        elif os.path.isdir(source_path):
                os.mkdir(dest_path)
                print(f'created directory {dest_path}')
                create_static(source_path, dest_path)
        

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
    



if __name__ == "__main__":
    main()
