from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
from extract_markdown_items import extract_markdown_items
from enum import Enum


def get_opening_symbol(text_type: TextType) -> str:
    if text_type == TextType.IMAGE:
        return "!["
    elif text_type == TextType.LINK:
        return "["
    else:
        raise ValueError(f"Unsupported item type: {text_type}")


def split_nodes_items(old_nodes: list[TextNode], text_type: TextType) -> list[TextNode]:
    """
    Splits the text of TextNode objects into separate nodes based on markdown image and link syntax.

    Args:
        old_nodes (list[TextNode]): A list of TextNode objects to be split.
    """
    new_nodes: list[TextNode] = []
    node_images = extract_markdown_items(
        " ".join([node.text for node in old_nodes if node.text_type == TextType.TEXT]),
        text_type,
    )
    if not node_images:
        return old_nodes
    opening_symbol = get_opening_symbol(text_type)
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            for item_text, item_link in node_images:
                sections = node.text.split(
                    f"{opening_symbol}{item_text}]({item_link})", 1
                )
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT, node.url))
                new_nodes.append(TextNode(item_text, text_type, item_link))
                node.text = sections[
                    1
                ]  # Update the node text to the remaining section for further processing
        return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes_items(old_nodes, TextType.IMAGE)


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes_items(old_nodes, TextType.LINK)
