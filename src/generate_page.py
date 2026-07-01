import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown: str) -> str:
    """
    Extracts the title from a markdown string. The title is defined as the first line that starts with a '#' character.
    If no title is found, an empty string is returned.

    Args:
        markdown (str): The markdown string to extract the title from.

    Returns:
        str: The extracted title or an empty string if no title is found.
    """
    for line in markdown.splitlines():
        stripped_line = line.strip()
        if stripped_line.startswith("# "):
            return stripped_line.lstrip("# ").strip()
    return ""

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()
    # html_content = template_content.replace("{{ title }}", title).replace("{{ content }}", markdown_content)
    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    html_page = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html_page)