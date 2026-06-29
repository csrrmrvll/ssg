from inline_markdown import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType
from inline_markdown import Delimiter, split_nodes_delimiter


def print_nodes(nodes):
    for node in nodes:
        print(f"Node: {node}")


def text_to_textnodes(text: str) -> list[TextNode]:
    """
    Converts a string of Markdown text into a list of TextNode objects.

    Args:
        text (str): The input text to be converted.

    Returns:
        list[TextNode]: A list of TextNode objects representing the input text.
    """
    if not text:
        return []
    nodes = split_nodes_delimiter(
        [TextNode(text, TextType.TEXT)], Delimiter.BOLD.value, TextType.BOLD
    )
    nodes = split_nodes_delimiter(nodes, Delimiter.ITALIC.value, TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, Delimiter.CODE.value, TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
