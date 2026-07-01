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
