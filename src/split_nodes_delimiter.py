from textnode import TextNode, TextType
from enum import Enum

class Delimiter(Enum):
    SPACE = " "
    COMMA = ","
    SEMICOLON = ";"
    COLON = ":"
    PERIOD = "."
    EXCLAMATION = "!"
    QUESTION = "?"
    NEWLINE = "\n"
    BOLD = "**"
    ITALIC = "_"
    CODE = "`"

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    if delimiter not in [d.value for d in Delimiter]:
        raise ValueError(f"Unsupported delimiter: {delimiter}")
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        assert node.text_type == TextType.TEXT, f"Node text_type must be {TextType.TEXT}, got {node.text_type}"
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            parts = node.text.split(delimiter)
            for i, part in enumerate(parts):
                if part:
                    new_nodes.append(TextNode(part, text_type, node.url))
                if i < len(parts) - 1:
                    new_nodes.append(TextNode(delimiter, text_type, node.url))
    return new_nodes
