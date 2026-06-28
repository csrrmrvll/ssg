import re


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    """
    Extracts image URLs and alt text from markdown text.

    Args:
        text (str): The markdown text to extract image URLs from.

    Returns:
        list[tuple[str, str]]: A list of tuples containing alt text and image URLs.
    """
    # Regular expression to match markdown image syntax ![alt text](image_url)
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    """
    Extracts link URLs and link text from markdown text.

    Args:
        text (str): The markdown text to extract link URLs from.

    Returns:
        list[tuple[str, str]]: A list of tuples containing link text and link URLs.
    """
    # Regular expression to match markdown link syntax [link text](link_url)
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)
