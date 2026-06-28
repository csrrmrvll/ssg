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

# def get_text_type_from_delimiter(delimiter: str) -> TextType:
#     if delimiter == Delimiter.BOLD.value:
#         return TextType.BOLD
#     elif delimiter == Delimiter.ITALIC.value:
#         return TextType.ITALIC
#     elif delimiter == Delimiter.CODE.value:
#         return TextType.CODE
#     else:
#         raise ValueError(f"Unsupported delimiter for text type: {delimiter}")

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    if delimiter not in [d.value for d in Delimiter]:
        raise ValueError(f"Unsupported delimiter: {delimiter}")
    new_nodes: list[TextNode] = []
    needs_closing_delimiter = False
    if text_type in [TextType.BOLD, TextType.ITALIC, TextType.CODE]:
        needs_closing_delimiter = True
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text == "":
            continue  # Skip empty nodes
        parts = node.text.split(delimiter)
        if needs_closing_delimiter and len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text}")
        for i, part in enumerate(parts):
            if part == "":
                continue
            if needs_closing_delimiter and i % 2 == 1:
                # This part is between delimiters, so it should be of the specified text_type
                node_text_type = text_type
            else:
                # This part is outside delimiters, so it should be of type TEXT
                node_text_type = TextType.TEXT
            node = TextNode(part, node_text_type, node.url)
            new_nodes.append(node)
    return new_nodes
