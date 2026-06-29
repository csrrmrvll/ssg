from inline_markdown import split_nodes_delimiter
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
    new_nodes: list[TextNode] = []
    matches = extract_markdown_items(
        " ".join([node.text for node in old_nodes if node.text_type == TextType.TEXT]),
        text_type,
    )
    if not matches:
        return old_nodes
    opening_symbol = get_opening_symbol(text_type)
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for item_text, item_link in matches:
            if f"{opening_symbol}{item_text}]({item_link})" in old_node.text:
                split_nodes = remaining_text.split(
                    f"{opening_symbol}{item_text}]({item_link})", 1
                )
                if len(split_nodes) < 2:
                    continue  # Skip if the item is not found in the current node's text
                first = split_nodes[0]
                second = split_nodes[1]
                if first != "":
                    new_nodes.append(TextNode(first, TextType.TEXT, old_node.url))
                new_nodes.append(TextNode(item_text, text_type, item_link))
                remaining_text = second  # Update remaining_text to the second part for further splitting
                if remaining_text == "":
                    break  # No more text to process in this node
        if remaining_text != "" and remaining_text not in [n.text for n in new_nodes]:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT, old_node.url))
    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes_items(old_nodes, TextType.IMAGE)


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes_items(old_nodes, TextType.LINK)
