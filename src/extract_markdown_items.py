import re
from textnode import TextType


def extract_markdown_items(text: str, text_type: TextType) -> list[tuple[str, str]]:
    """
    Extracts link URLs and link text from markdown text.

    Args:
        text (str): The markdown text to extract link URLs from.

    Returns:
        list[tuple[str, str]]: A list of tuples containing link text and link URLs.
    """
    if text_type == TextType.IMAGE:
        return extract_markdown_images(text)
    elif text_type == TextType.LINK:
        return extract_markdown_links(text)
    raise ValueError("Unsupported markdown item type")


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    # Regular expression to match markdown image syntax ![alt text](image_url)
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    # Regular expression to match markdown link syntax [link text](link_url)
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)
