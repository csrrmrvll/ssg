from inline_markdown import text_to_textnodes
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
import re

from textnode import TextType


def text_to_children(text) -> list[HTMLNode]:
    nodes = []
    blocks = markdown_to_blocks(text)
    for block in blocks:
        text_nodes = text_to_textnodes(block)
        for text_node in text_nodes:
            if text_node.text_type == TextType.TEXT:
                nodes.append(LeafNode("", text_node.text.replace("\n", " ")))
            elif text_node.text_type == TextType.BOLD:
                nodes.append(LeafNode("b", text_node.text))
            elif text_node.text_type == TextType.ITALIC:
                nodes.append(LeafNode("i", text_node.text))
            elif text_node.text_type == TextType.CODE:
                nodes.append(LeafNode("code", text_node.text))
            elif text_node.text_type == TextType.IMAGE:
                nodes.append(
                    LeafNode(
                        "img",
                        "",
                        {"src": text_node.src, "alt": text_node.alt},
                    )
                )
            elif text_node.text_type == TextType.LINK:
                nodes.append(LeafNode("a", text_node.text, {"href": text_node.href}))
    return nodes


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            nodes = text_to_children(block)
            children.append(ParentNode("p", nodes))
        elif block_type == BlockType.HEADING:
            level = len(re.match(r"^(#+)", block).group(1))
            content = block[level + 1 :].strip()
            nodes = text_to_children(content)
            children.append(ParentNode(f"h{level}", nodes))
        elif block_type == BlockType.CODE:
            content = block[4:-3]
            children.append(ParentNode("pre", [LeafNode("code", content)]))
        elif block_type == BlockType.QUOTE:
            content = re.sub(r"^> ?", "", block, flags=re.MULTILINE)
            nodes = text_to_children(content)
            children.append(ParentNode("blockquote", [ParentNode("p", nodes)]))
        elif block_type == BlockType.ULIST:
            items = re.findall(r"^- (.*)", block, re.MULTILINE)
            list_parent = ParentNode("ul")
            list_children = [LeafNode("li", item) for item in items]
            list_parent.children = list_children
            children.append(list_parent)
        elif block_type == BlockType.OLIST:
            items = re.findall(r"^\d+\. (.*)", block, re.MULTILINE)
            list_parent = ParentNode("ol")
            list_children = [LeafNode("li", item) for item in items]
            list_parent.children = list_children
            children.append(list_parent)
    parent_node = ParentNode("div", children)
    return parent_node
