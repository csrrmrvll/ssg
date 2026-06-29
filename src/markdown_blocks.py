from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    if re.search(r"^#{1,6} .*\n", block):
        return BlockType.HEADING
    elif block.startswith("```\n") and block.endswith("\n```"):
        return BlockType.CODE
    elif re.search(r"^> ?.*", block, re.MULTILINE):
        return BlockType.QUOTE
    elif re.search(r"^- .*", block, re.MULTILINE):
        return BlockType.UNORDERED_LIST
    elif re.search(r"^\d+\. .*", block, re.MULTILINE):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def markdown_to_blocks(markdown: str) -> list[str]:
    lines = markdown.split("\n\n")
    blocks = []
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        blocks.append(line)
    return blocks
